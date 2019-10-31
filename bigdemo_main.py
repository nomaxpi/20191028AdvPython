#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_bigdemo import Ui_BigDemo


class BigDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_BigDemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        #   self.ui.actionQuit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)
        self.ui.button_go.clicked.connect(self._pushed)

    def _pushed(self):
        print("You pushed the button")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BigDemoMain()
    main.show()
    sys.exit(app.exec_())


