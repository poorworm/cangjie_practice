import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from main_gui import Ui_MainWindow
from main_gui_sub import Ui_MainWindow_Sub

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow_Sub()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())