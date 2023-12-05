from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from ea_barcode import send_to_print

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Print barcode')
        self.setFixedSize(500, 400)
        
        btn_push = QPushButton('PRINT IT')
        btn_push.setCheckable(True)
        btn_push.clicked.connect(self.btn_press_event)
        
        self.setCentralWidget(btn_push)

    def btn_press_event(self):
        send_to_print(1)

def init_gui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
