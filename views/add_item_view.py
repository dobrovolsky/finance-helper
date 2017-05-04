from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QDialog

from model.models import Category, Item
from views.add_item import Ui_Dialog
from views.add_category_view import AddCategory
from model.model_wrapper import ModelWrapper


class AddItem(Ui_Dialog):
    def __init__(self, Dialog, connector, url, item=None):
        super(AddItem, self).__init__()
        self.Connector = connector
        self.db_url = url
        self.dialog = Dialog
        self.session = self.Connector(db=self.db_url).session
        self.item_list = item
        self.setup_ui()
        self.setup_actions()
        Dialog.exec_()

    def setup_ui(self):
        super(AddItem, self).setupUi(self.dialog)
        self.set_categories()
        if self.item_list:
            self.item_list = self.session.query(Item).get(self.item_list)
            self.name_editor.insert(self.item_list.name)
            self.price_spin.setValue(self.item_list.price)
            self.count_split.setValue(self.item_list.count)
            self.description_editor.insert(self.item_list.description)
            self.category_selector.setCurrentText(self.item_list.category.name)
            self.date_editor.setDate(QDate(self.item_list.date))
            self.remove_button.setEnabled(True)

    def setup_actions(self):
        self.cancel_button.clicked.connect(self.dialog.close)
        self.cancel_button.setShortcut('Ctrl+Q')

        self.add_category_button.clicked.connect(self.open_add_category)
        self.save_button.clicked.connect(self.save_item)

        self.remove_button.clicked.connect(self.delete_item)

    def set_categories(self):
        self.category_selector.clear()
        for category in self.session.query(Category).all():
            self.category_selector.addItem(category.name, category.id)

    def open_add_category(self):
        dialog = QDialog()
        AddCategory(dialog, connector=self.Connector, url=self.db_url)
        self.set_categories()

    def save_item(self):
        name = self.name_editor.text()
        price = self.price_spin.value()
        count = self.count_split.value()
        description = self.description_editor.text()
        category_id = self.category_selector.currentData()
        date = QDateTime(self.date_editor.date()).toPyDateTime()
        if self.item_list:
            self.item_list.name = name
            self.item_list.price = price
            self.item_list.count = count
            self.item_list.description = description
            self.item_list.category_id = category_id
            self.item_list = date
        else:
            item = ModelWrapper.add_item(name=name, price=price, count=count, category_id=category_id,
                                         description=description, date=date, user_id=1)
            self.session.add(item)
        self.session.commit()
        self.dialog.close()

    def delete_item(self):
        self.session.delete(self.item_list)
        self.session.commit()
        self.dialog.close()
