from PyQt6.QtCore import Qt, QSize, QPoint, QRect
from PyQt6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, QPushButton, QLineEdit, QComboBox, QHBoxLayout, QRadioButton, QButtonGroup
import sys
import sqlite3
import time



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme = "dark"
        self.setWindowTitle("Russia population checker")
        self.setGeometry(600, 200, 800, 600)


        self.label1 = QLabel("Last date:")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label1.setStyleSheet("font-size:24px; font-weight:bold; font-family:Times New Roman; border: 1px solid blue; ")
        self.label2 = QLabel("Last count:")
        self.label2.setStyleSheet(
            "font-size:24px; font-weight:bold; font-family:Times New Roman;")
        self.label3 = QLabel("Previous data:")
        self.label3.setStyleSheet(
            "font-size:24px; font-weight:bold; font-family:Times New Roman;")
        self.button = QPushButton("Update")
        self.button2 = QPushButton("Get data (The update will be performed automatically.)")

        self.button.setStyleSheet("font-size:24px; font-weight:bold; font-family:Times New Roman;")
        self.button.setFixedSize(200, 70)
        self.button.clicked.connect(self.update_info)
        self.button2.clicked.connect(self.c_parse)
        self.combo = QComboBox()


        layout = QVBoxLayout()

        pred_layout = QHBoxLayout()

        layout.addWidget(self.button)
        layout.setAlignment(self.button, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label1)
        layout.addSpacing(70)
        layout.addWidget(self.label2)
        layout.addSpacing(70)

        pred_layout.addWidget(self.combo)
        pred_layout.addSpacing(70)
        pred_layout.addWidget(self.label3)

        layout.addLayout(pred_layout)
        layout.addSpacing(70)
        layout.addWidget(self.button2)
        con = QWidget()
        con.setLayout(layout)

        self.setCentralWidget(con)

        self.last_data = ()
        self.prev_data = ()
        self.data = []

    def update_info(self):
        with sqlite3.connect('db.sqlite3') as con:
            cursor = con.cursor()

            self.data = cursor.execute('SELECT count, date FROM data').fetchall()
            self.combo.clear()
            self.combo.addItems([a[1] + " " + str(a[0]) for a in self.data[::-1]])
            print(self.data)

            if len(self.data) > 0:



                if self.data[-1] != self.last_data:
                    self.last_data = self.data[-1]
            if len(self.data) > 1:
                for i in self.data[::-1]:
                    if i[-1] !=self.last_data[-1]:
                        self.prev_data = i
                        break


        try:
            self.label1.setText(f"Last date: {self.last_data[-1]}")
            self.label2.setText(f"Last count: {self.last_data[0]}")
        except:
            pass
        try:
            self.label3.setText(f"Previous data: {self.prev_data[-1]}, {self.prev_data[0]}")
        except:
            pass
    def change_theme(self):
        if self.theme == "dark":
            self.setStyleSheet("background-color:black")
        self.label1.setStyleSheet("color:white")
        self.label2.setStyleSheet("color:white")
        self.label3.setStyleSheet("color:white")
        self.button.setStyleSheet("color:white")
        self.combo.setStyleSheet("color:white")
    def c_parse(self) -> None:
        print("parse")
        time.sleep(15)
        self.update()
app = QApplication(sys.argv)
window = MainWindow()
window.update_info()
window.show()
app.exec()