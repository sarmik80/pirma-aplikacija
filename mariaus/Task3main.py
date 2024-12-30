# Sukurkite vartotojo sąsają kurioje matomas vienas laukelis į kurį vartotojas gali įvesti pasirinktą adresą.
#  Pvz: https://www.skelbimai.lt/skelbimai/darbas-verslas/iesko-darbo 

# Adresas gali būti įvedamas tik iš puslapio skelbimai.lt ir tai gali būti tik kategorijos puslapis.

# Surinkite visų skelbimų duomenis ir vartotojui sąsajoje grąžinkite kiek iš viso skelbimų radote.



from PyQt6.QtWidgets import QApplication, QMainWindow
from Task3UI import Ui_MainWindow
import requests
from bs4 import BeautifulSoup
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(self.collect_inputs)

    def collect_inputs(self):
        url = self.ui.Input_web.text()
        if "https://www.skelbimai.lt" in url:
            data = requests.get(url)
            html = BeautifulSoup(data.text, "html.parser") 
            category = html.select_one("span.item-wp.last > span")
            category = category.text.strip()

            number = html.select_one("div.description.f")
            number = number.text.strip()
            self.ui.Text.setText(f"{category} {number}")
        else:
            self.ui.Text.setText(f"{url} netinkamas web puslapis")  

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Input Form")
    window.show()
    app.exec()