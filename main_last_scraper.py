from PyQt6.QtWidgets import QApplication, QMainWindow
from last_scraper import Ui_MainWindow

import requests
from bs4 import BeautifulSoup
from time import sleep

class Window(QMainWindow, Ui_MainWindow) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pateikti.clicked.connect(self.pateikimas)

    def pateikimas(self):
        # Kai bus paspaustas mygtukas
        
        ivesta_nuoroda = self.nuoroda.text()


        rasta = self.scraper()
        self.rezultatas.setText(f"{pavadinimas}")


        data = requests.get(url)
        data = data.text
        html = BeautifulSoup(data, "html.parser")


        pavadinimas = html.select_one("#breadcrumb > div.description.f").text


app = QApplication([])

window = Window()

window.show()
app.exec()