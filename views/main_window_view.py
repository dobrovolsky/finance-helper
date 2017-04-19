import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QDialog, QMessageBox
from sqlalchemy.exc import IntegrityError

from model.alchemical_table_model import AlchemicalTableModel
from model.connector import Connector

from model.models import ItemList, Category, Item
from views.add_item_view import AddItem
from views.mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, main_window, connector, url):
        super(MainWindow, self).__init__()
        self.main_window = main_window
        self.Connector = connector
        self.db_url = url
        self.role = Qt.UserRole
        self.setup_ui(main_window)
        self.setup_actions()
        main_window.show()

    def setup_actions(self):
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.triggered.connect(QApplication.instance().quit)

        self.show_query_button.clicked.connect(self.change_model)
        self.add_item_button.clicked.connect(self.open_add_item)

        self.remove_category_button.clicked.connect(self.remove_category)

    def setup_ui(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        self.set_model()
        self.set_categories()

    def set_model(self, query=None):
        session = self.Connector(db=self.db_url).session
        if not query:
            query = session.query(ItemList)
        model = AlchemicalTableModel(session, query,
                                     [
                                         ('Name', ItemList, ('item', 'name'), {'editable': True}),
                                         ('Price', ItemList, ('item', 'price'), {'editable': True}),
                                         ('Count', ItemList, ('item', 'count'), {'editable': True}),
                                         ('Description', ItemList, ('item', 'description'), {'editable': True}),
                                         ('Category', ItemList, ('item', 'category', 'name'), {}),
                                         ('Date', ItemList, ('date',), {}),
                                     ])
        self.items_table.setModel(model)

    def set_categories(self):
        self.categories_list.clear()
        session = self.Connector(db=self.db_url).session
        for category in session.query(Category).all():
            item = QListWidgetItem(category.name)
            item.setData(self.role, category.id)
            self.categories_list.addItem(item)

    def change_model(self):
        session = self.Connector(db=self.db_url).session
        try:
            query = session.query(ItemList).join(Item).join(Category).filter(
                Category.id == self.categories_list.selectedItems()[0].data(self.role))
            self.set_model(query)
        except IndexError:
            self.set_model()

    def open_add_item(self):
        dialog = QDialog()
        AddItem(dialog, self.Connector(db=self.db_url).session)

    def remove_category(self):
        try:
            session = Connector(db=os.environ['DB']).session
            category = session.query(Category).get(self.categories_list.selectedItems()[0].data(self.role))
            session.delete(category)
            session.commit()
            self.set_categories()
        except IndexError:
            QMessageBox.information(None, 'Error', 'Please, select category item before delete them')
        except IntegrityError:
            QMessageBox.information(None, 'Error', 'You can\'t delete category that refers to item')
