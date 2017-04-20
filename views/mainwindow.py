# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(834, 460)
        MainWindow.setMinimumSize(QtCore.QSize(834, 460))
        MainWindow.setMaximumSize(QtCore.QSize(834, 460))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 8, 151, 390))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.categories_lable = QtWidgets.QLabel(self.formLayoutWidget)
        self.categories_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.categories_lable.setObjectName("categories_lable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.categories_lable)
        self.remove_category_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.remove_category_button.setObjectName("remove_category_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.remove_category_button)
        self.categories_list = QtWidgets.QListWidget(self.formLayoutWidget)
        self.categories_list.setMinimumSize(QtCore.QSize(0, 140))
        self.categories_list.setObjectName("categories_list")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.categories_list)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.periond_start = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.periond_start.setEnabled(False)
        self.periond_start.setCalendarPopup(True)
        self.periond_start.setDate(QtCore.QDate(2017, 4, 18))
        self.periond_start.setObjectName("periond_start")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.periond_start)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.periond_finish = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.periond_finish.setEnabled(False)
        self.periond_finish.setCalendarPopup(True)
        self.periond_finish.setDate(QtCore.QDate(2017, 4, 18))
        self.periond_finish.setObjectName("periond_finish")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.periond_finish)
        self.show_query_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.show_query_button.setObjectName("show_query_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.show_query_button)
        self.user_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.user_label)
        self.change_user_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.change_user_button.setObjectName("change_user_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.change_user_button)
        self.periond_checkbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.periond_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.periond_checkbox.setObjectName("periond_checkbox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.periond_checkbox)
        self.add_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_item_button.setGeometry(QtCore.QRect(670, 380, 151, 22))
        self.add_item_button.setObjectName("add_item_button")
        self.items_table = QtWidgets.QTableWidget(self.centralwidget)
        self.items_table.setGeometry(QtCore.QRect(170, 10, 651, 361))
        self.items_table.setObjectName("items_table")
        self.items_table.setColumnCount(0)
        self.items_table.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_export_to_excel = QtWidgets.QAction(MainWindow)
        self.action_export_to_excel.setObjectName("action_export_to_excel")
        self.action_import_from_excel = QtWidgets.QAction(MainWindow)
        self.action_import_from_excel.setObjectName("action_import_from_excel")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menuFile.addAction(self.action_export_to_excel)
        self.menuFile.addAction(self.action_import_from_excel)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Your finance manager"))
        self.categories_lable.setText(_translate("MainWindow", "Categories"))
        self.remove_category_button.setText(_translate("MainWindow", "Remove category"))
        self.label_3.setText(_translate("MainWindow", "Start"))
        self.periond_start.setDisplayFormat(_translate("MainWindow", "M/dd/yyyy"))
        self.label_5.setText(_translate("MainWindow", "Finish"))
        self.periond_finish.setDisplayFormat(_translate("MainWindow", "M/dd/yyyy"))
        self.show_query_button.setText(_translate("MainWindow", "Show"))
        self.user_label.setText(_translate("MainWindow", "UserName"))
        self.change_user_button.setText(_translate("MainWindow", "Change User"))
        self.periond_checkbox.setText(_translate("MainWindow", "Filter by date"))
        self.add_item_button.setText(_translate("MainWindow", "Add item"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_export_to_excel.setText(_translate("MainWindow", "Export to Excel"))
        self.action_import_from_excel.setText(_translate("MainWindow", "Import from Excel"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))

