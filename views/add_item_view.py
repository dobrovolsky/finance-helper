

from views.add_item import Ui_Dialog


class AddItem(Ui_Dialog):
    def __init__(self, Dialog, categories):
        super(AddItem, self).__init__()
        self.categories = categories
        self.setup_ui(Dialog)
        self.setup_actions(Dialog)
        Dialog.exec_()

    def setup_ui(self, Dialog):
        super(AddItem, self).setupUi(Dialog)
        self.set_categories()

    def setup_actions(self, Dialog):
        self.cancel_button.clicked.connect(Dialog.close)
        self.cancel_button.setShortcut('Ctrl+Q')

    def set_categories(self):
        for category in self.categories:
            self.category_selector.addItem(category.name)
