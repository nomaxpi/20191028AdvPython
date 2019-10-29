#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import Qt

from ui_chicagosalaries import Ui_ChicagoSalaries

from chicagodata import get_row_count, get_salary_data_as_list

class SalaryItem(QTableWidgetItem):
    def __lt__(self, other):
        return self.data(Qt.UserRole) < other.data(Qt.UserRole)

class ChicagoSalariesMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_ChicagoSalaries()
        self.ui.setupUi(self)

        self._load_table()

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def _load_table(self):
        num_rows = get_row_count()
        self.ui.table_salary.setRowCount(num_rows)
        for row_id, row_data in enumerate(get_salary_data_as_list(num_rows)):
            for column_id, column_data in enumerate(row_data):
                if column_id == 3: # salary data
                    display_data = f"${column_data:.02f}"
                    table_item = SalaryItem(display_data)  # salary as str
                    table_item.setData(Qt.UserRole, column_data) # salary as float
                else:
                    table_item = QTableWidgetItem(column_data)

                self.ui.table_salary.setItem(row_id, column_id, table_item)
                # add row to table

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ChicagoSalariesMain()
    main.show()
    sys.exit(app.exec_())


