# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_category.ui'
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
        self.name_editor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_editor.setObjectName("name_editor")
        self.gridLayout.addWidget(self.name_editor, 1, 1, 1, 2)
        self.lable_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lable_name.setMinimumSize(QtCore.QSize(90, 0))
        self.lable_name.setMaximumSize(QtCore.QSize(45, 16777215))
        self.lable_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_name.setObjectName("lable_name")
        self.gridLayout.addWidget(self.lable_name, 1, 0, 1, 1)
        self.lable_description = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lable_description.setMinimumSize(QtCore.QSize(90, 0))
        self.lable_description.setMaximumSize(QtCore.QSize(45, 16777215))
        self.lable_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_description.setObjectName("lable_description")
        self.gridLayout.addWidget(self.lable_description, 2, 0, 1, 1)
        self.description_editor = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.description_editor.setObjectName("description_editor")
        self.gridLayout.addWidget(self.description_editor, 2, 1, 1, 1)
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
        Dialog.setWindowTitle(_translate("Dialog", "Add category"))
        self.lable_name.setText(_translate("Dialog", "name"))
        self.lable_description.setText(_translate("Dialog", "description"))
        self.save_button.setText(_translate("Dialog", "Save"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.reset_button.setText(_translate("Dialog", "Reset"))

