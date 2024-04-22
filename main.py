import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QPixmap
import requests
from datetime import datetime


class ApplicationWeather(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather")
        self.setGeometry(100, 100, 500, 500)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.central_widget.setStyleSheet("background-color:#e3d1a1")

        self.label_city = QLabel('Місто', self)
        self.layout.addWidget(self.label_city)

        self.city_combo = QComboBox(self)
        self.city_combo.addItems(["Львів", "Київ", "Одеса", "Харків", "Ужгород", "Миколаїв", "Вінниця", "Житомир", "Тернопіль"])
        self.layout.addWidget(self.city_combo)

        # self.city_combo.currentIndexChanged.connect(self.get_wather)
        self.city_combo.setStyleSheet("""
            QComboBox {
                background-color: #fff;
                border: 1px solid #ccc
                padding: 5px;
                border-radius: 3px;
            }
            QComboBox::drop-down {
                border: none;
            }


        """)



app = QApplication(sys.argv)
window = ApplicationWeather()
window.show()
sys.exit(app.exec_())
