from PyQt5.QtWidgets import QApplication, QMainWindow

from ea_barcode import send_to_print
from ea_barcode import get_config
from ea_barcode import write_new_last_num
from ea_barcode import write_new_prefix
from layout.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    num_to_print = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        config = get_config()
        prefix = config['BARCODE']['PREFIX']
        self.code_text.setText(prefix)
        next_barcode = int(config['BARCODE']['NEXT_BARCODE'])
        self.code_num_box.setValue(next_barcode)
        (self.num_to_print_box.valueChanged
         .connect(self.box_num_to_print_edit_event))
        self.print_btn.clicked.connect(self.btn_print_event)
        self.code_text.textChanged.connect(self.code_text_change_event)
        self.code_num_box.valueChanged.connect(self.box_code_num_change_event)

    def btn_print_event(self):
        send_to_print(self.num_to_print)
        config = get_config()
        new_barcode = int(config['BARCODE']['NEXT_BARCODE'])
        self.code_num_box.setValue(new_barcode)

    def box_num_to_print_edit_event(self, new_num):
        self.num_to_print = new_num

    def box_code_num_change_event(self, new_code):
        write_new_last_num(new_code)

    def code_text_change_event(self, new_text):
        if new_text:
            write_new_prefix(new_text)


def init_gui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
