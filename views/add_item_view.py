from PyQt5.QtWidgets import QDialog

from model.models import Category
from views.add_item import Ui_Dialog
from views.add_category_view import AddCategory


class AddItem(Ui_Dialog):
    def __init__(self, Dialog, session):
        super(AddItem, self).__init__()
        self.session = session
        self.setup_ui(Dialog)
        self.setup_actions(Dialog)
        Dialog.exec_()

    def setup_ui(self, Dialog):
        super(AddItem, self).setupUi(Dialog)
        self.set_categories()

    def setup_actions(self, Dialog):
        self.cancel_button.clicked.connect(Dialog.close)
        self.cancel_button.setShortcut('Ctrl+Q')

        self.add_category_button.clicked.connect(self.open_add_category)

    def set_categories(self):
        self.category_selector.clear()
        for category in self.session.query(Category).all():
            self.category_selector.addItem(category.name)

    def open_add_category(self):
        dialog = QDialog()
        AddCategory(dialog, self.session)
        self.set_categories()
