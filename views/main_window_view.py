import os

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QDialog, QMessageBox, QListWidgetItem, QFileDialog
from sqlalchemy.exc import IntegrityError

from excel.export import ExcelExport
from model.connector import Connector

from model.models import Category, Item, User
from views.add_item_view import AddItem
from views.mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, main_window, connector, url):
        super(MainWindow, self).__init__()
        self.main_window = main_window
        self.table_header = ('name', 'price', 'count', 'description', 'category', 'date')
        self.row_items = (
            ('name',), ('price',), ('count',), ('description',),
            ('category', 'name'), ('date',))
        self.Connector = connector
        self.db_url = url
        self.setup_ui(main_window)
        self.setup_actions()
        main_window.show()

    def setup_actions(self):
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.triggered.connect(QApplication.instance().quit)

        self.show_query_button.clicked.connect(self.set_items)
        self.add_item_button.clicked.connect(self.add_item)

        self.remove_category_button.clicked.connect(self.remove_category)
        self.periond_checkbox.clicked.connect(self.change_date_input)
        self.action_export_to_excel.triggered.connect(self.export_to_excel)

    def setup_ui(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        self.items_table.itemDoubleClicked.connect(self.edit_item)
        self.restart_ui()

    def restart_ui(self):
        self.items_table.setHorizontalHeaderLabels(self.table_header)
        self.set_items()
        self.set_user_name()
        self.set_categories()

    def set_user_name(self):
        session = self.Connector(db=self.db_url).session
        user = session.query(User).get(1)
        self.user_label.setText(user.first_name + ' ' + user.last_name)

    def set_items(self):
        self.items_table.clear()
        query = self.get_query()
        self.items_table.setRowCount(query.count())
        self.items_table.setColumnCount(len(self.table_header))
        for item_list in enumerate(query):
            for row_item in enumerate(self.row_items):
                last_value = getattr(item_list[1], row_item[1][0])
                for attr in row_item[1][1:]:
                    last_value = getattr(last_value, attr)
                item = QTableWidgetItem(str(last_value))
                item.setData(Qt.UserRole, item_list[1].id)
                item.setFlags(Qt.ItemIsEnabled)
                self.items_table.setItem(item_list[0], row_item[0], item)

    def set_categories(self):
        self.categories_list.clear()
        session = self.Connector(db=self.db_url).session
        for category in session.query(Category).all():
            item = QListWidgetItem(category.name)
            item.setData(Qt.UserRole, category.id)
            self.categories_list.addItem(item)

    def edit_item(self, item):
        dialog = QDialog()
        AddItem(dialog, self.Connector, url=self.db_url, item=item.data(Qt.UserRole))
        self.restart_ui()

    def get_query(self):
        session = self.Connector(db=self.db_url).session
        query = session.query(Item).join(Category)
        if self.periond_checkbox.isChecked():
            start_date = QDateTime(self.periond_start.date()).toPyDateTime()
            finish_date = QDateTime(self.periond_finish.date()).toPyDateTime()
            query = query.filter(Item.date >= start_date, Item.date <= finish_date)
        try:
            query = query.filter(Category.id == self.categories_list.selectedItems()[0].data(Qt.UserRole))
        except IndexError:
            pass
        return query.order_by(Item.date)

    def add_item(self):
        dialog = QDialog()
        AddItem(dialog, self.Connector, url=self.db_url)
        self.restart_ui()

    def remove_category(self):
        try:
            session = Connector(db=os.environ['DB']).session
            category = session.query(Category).get(self.categories_list.selectedItems()[0].data(Qt.UserRole))
            session.delete(category)
            session.commit()
            self.restart_ui()
        except IndexError:
            QMessageBox.information(None, 'Error', 'Please, select category item before delete them')
        except IntegrityError:
            QMessageBox.information(None, 'Error', 'You can\'t delete category that refers to item')

    def change_date_input(self):
        self.periond_start.setEnabled(self.periond_checkbox.isChecked())
        self.periond_finish.setEnabled(self.periond_checkbox.isChecked())

    def export_to_excel(self):
        dialog = QFileDialog()
        filename = dialog.getSaveFileName()
        if filename[0]:
            ExcelExport().create_file(filename[0], self.get_query(), 'saved items')
