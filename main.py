import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow

from model.connector import Connector
from views.main_window_view import MainWindow


app = QApplication(sys.argv)
main_window = QMainWindow()
window = MainWindow(main_window, Connector(db=os.environ['DB']).session)
sys.exit(app.exec_())
