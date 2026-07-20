#from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication
import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Russia population checker")
        self.setMinimumSize(300, 500)
        self.label = QLabel("Russia Population Checker")
        self.label1 = QLabel("Date:")
        self.label2 = QLabel("Count:")
        self.label3 = QLabel("Previous:")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        con = QWidget()
        con.setLayout(layout)
        self.setCentralWidget(con)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()