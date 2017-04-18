from PyQt5.QtWidgets import QApplication, QListWidgetItem, QDialog
from model.alchemical_table_model import AlchemicalTableModel

from model.models import ItemList, Category, Item
from views.add_item_view import AddItem
from views.mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, main_window, session):
        super(MainWindow, self).__init__()
        self.main_window = main_window
        self.session = session
        self.setup_ui(main_window)
        self.setup_actions()
        main_window.show()

    def setup_actions(self):
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.triggered.connect(QApplication.instance().quit)

        self.show_query_button.clicked.connect(self.change_model)
        self.add_item_button.clicked.connect(self.open_about)

    def setup_ui(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        self.set_model()
        self.set_categories()

    def set_model(self, query=None):
        if not query:
            query = self.session.query(ItemList)
        model = AlchemicalTableModel(self.session, query,
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
        for category in self.session.query(Category).all():
            self.categories_list.addItem(QListWidgetItem(category.name))

    def change_model(self):
        try:
            query = self.session.query(ItemList).join(Item).join(Category).filter(
                Category.name == self.categories_list.selectedItems()[0].text())
            self.set_model(query)
        except IndexError:
            self.set_model()

    def open_about(self):
        dialog = QDialog()
        AddItem(dialog, self.session.query(Category).all())