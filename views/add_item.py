# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_item.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 245)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.category_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.category_label.setAlignment(QtCore.Qt.AlignCenter)
        self.category_label.setObjectName("category_label")
        self.gridLayout.addWidget(self.category_label, 3, 0, 1, 1)
        self.price_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.price_label.setObjectName("price_label")
        self.gridLayout.addWidget(self.price_label, 2, 0, 1, 1)
        self.lable_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lable_name.setMaximumSize(QtCore.QSize(45, 16777215))
        self.lable_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_name.setObjectName("lable_name")
        self.gridLayout.addWidget(self.lable_name, 1, 0, 1, 1)
        self.name_editor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_editor.setObjectName("name_editor")
        self.gridLayout.addWidget(self.name_editor, 1, 1, 1, 2)
        self.price_editor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.price_editor.setObjectName("price_editor")
        self.gridLayout.addWidget(self.price_editor, 2, 1, 1, 2)
        self.date_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 5, 0, 1, 1)
        self.date_editor = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.date_editor.setCalendarPopup(True)
        self.date_editor.setObjectName("date_editor")
        self.gridLayout.addWidget(self.date_editor, 5, 1, 1, 2)
        self.category_selector = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.category_selector.setObjectName("category_selector")
        self.gridLayout.addWidget(self.category_selector, 3, 1, 1, 1)
        self.add_category_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_category_button.setMaximumSize(QtCore.QSize(83, 16777215))
        self.add_category_button.setObjectName("add_category_button")
        self.gridLayout.addWidget(self.add_category_button, 3, 2, 1, 1)
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setGeometry(QtCore.QRect(299, 210, 81, 22))
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(200, 210, 91, 22))
        self.cancel_button.setObjectName("cancel_button")
        self.reset_button = QtWidgets.QPushButton(Dialog)
        self.reset_button.setGeometry(QtCore.QRect(10, 210, 80, 22))
        self.reset_button.setObjectName("reset_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Item"))
        self.category_label.setText(_translate("Dialog", "category"))
        self.price_label.setText(_translate("Dialog", "price"))
        self.lable_name.setText(_translate("Dialog", "name"))
        self.date_label.setText(_translate("Dialog", "date"))
        self.date_editor.setDisplayFormat(_translate("Dialog", "Mm/dd/yyyy"))
        self.add_category_button.setText(_translate("Dialog", "Add category"))
        self.save_button.setText(_translate("Dialog", "Save"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.reset_button.setText(_translate("Dialog", "Reset"))

