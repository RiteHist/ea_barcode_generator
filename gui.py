from PyQt5.QtWidgets import QApplication, QMainWindow

from ea_barcode import send_to_print
from layout.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    num_to_print = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(400, 100)
        (self.num_to_print_box.valueChanged
         .connect(self.box_num_to_print_edit_event))
        self.print_btn.clicked.connect(self.btn_print_event)

    def btn_print_event(self):
        send_to_print(self.num_to_print)

    def box_num_to_print_edit_event(self, new_num):
        self.num_to_print = new_num


def init_gui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
