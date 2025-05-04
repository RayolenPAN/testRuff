from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    def initUI(self):
        self.index = QLabel('Индекс Руфье: 4.8')
        self.heart = QLabel('Работоспособность сердца: выше среднего')
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(index,alignment=Qt.AlignCenter)
        self.v_line.addWidget(heart,alignment=Qt.AlignCenter)
        self.layout_main = QHBoxLayout()
        self.layout_main.addLayout(v_line)
        self.my_wid.setLayout(layout_main)
    def set_appear(self):
        self.my_wid.setWindowTitle('Второй экран')
        self.my_wid.move(900,70)
        self.my_wid.resize(400,200)