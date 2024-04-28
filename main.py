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
        # self.city_combo.currentIndexChanged.connect(self.get_weather())

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
        self.button = QPushButton('Отримати погоду', self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.get_weather)
        self.button.setStyleSheet("""
            QpushButton {
                background-color: #007bff;
                color: #fff;
                padding: 7px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton: hover {
                background-color: #0056b3;

        
        """)

    def get_weather(self):
        api_key = 'f81703c1f3b81ad93e6644153c4a426e'
        city = self.city_combo.currentText()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data ['cod'] == 200:
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['main']['speed']
            icon_name = data['weather'][0]['icon']

            weather_text = f'Погода: {weather}\nТемпература: {temperature}℃\nВологість: {humidity}%\nШвидкість вітру:{wind_speed} м/с'
            self.weather_label.setText(weather_text)

            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(icon_name).content)
            self.icon_label.setPixmap(pixmap)

            now = datetime.now()
            formated_date = now.strftime("%d.%m.%Y %H:%M:%S")
            self.icon_label.setText(f"Останнє оновлення: (formatted_date) ")
        else:
            self.wheather_label.setText('Місто не знайдено.Спробуйте ще раз.')



app = QApplication(sys.argv)
window = ApplicationWeather()
window.show()
sys.exit(app.exec_())