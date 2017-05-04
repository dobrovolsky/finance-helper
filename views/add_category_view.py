from PyQt5.QtWidgets import QTextEdit, QMessageBox, QLineEdit

from model.models import Category
from views.add_category import Ui_Dialog
from model.model_wrapper import ModelWrapper


class AddCategory(Ui_Dialog):
    def __init__(self, Dialog, connector, url):
        super(AddCategory, self).__init__()
        self.Connector = connector
        self.db_url = url
        self.dialog = Dialog
        self.session = self.Connector(db=self.db_url).session
        self.setup_ui()
        self.setup_actions()
        self.dialog.exec_()

    def setup_ui(self):
        super(AddCategory, self).setupUi(self.dialog)

    def setup_actions(self):
        self.cancel_button.clicked.connect(self.dialog.close)
        self.cancel_button.setShortcut('Ctrl+Q')

        self.save_button.clicked.connect(self.add_category)

        self.reset_button.clicked.connect(self.reset_fields)

    def add_category(self):
        QTextEdit().toPlainText()
        self.session.add(ModelWrapper.add_category(name=self.name_editor.text(),
                                                   description=self.description_editor.toPlainText(),
                                                   user_id=1
                                                   ))
        self.session.commit()
        self.reset_fields()
        QMessageBox.information(None, 'Add category', 'Category was added')

    def reset_fields(self):
        self.name_editor.clear()
        self.description_editor.clear()