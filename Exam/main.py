from PyQt6.QtWidgets import QApplication, QMainWindow
from designexam import Ui_MainWindow

import requests
from bs4 import BeautifulSoup
from time import sleep

class Window(QMainWindow, Ui_MainWindow) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.enter_button.clicked.connect(self.scraped_data)

    def scraped_data(self):
        entered_url = self.url_field.text()

        if "https://elenta.lt/" in entered_url :
            response = []
            data = requests.get(entered_url)
            html = BeautifulSoup(data.text, "html.parser")
            data = html.select('.units-list li')
            title_sum = html.select_one("#summary-count > span")
            self.notification.setText(f"The scraper is currently collecting data")
            self.found.setText(f"The scraper has found {title_sum} ads whose value is eur")

            for listing in data :
                title = listing.select_one('a.ad-hyperlink')
                title = title.text if title else ""
            

                price = listing.select_one('.price-box')
                price = price.text if price else "0"

                response.append({
                    "title" : title,
                    "price" : price
                })

            next = html.select_one('[rel="next"]')

            sleep(1)
             
            if next :
                next = html.select_one('[rel="next"]').attrs['href']
                response += self.scraped_data(self)

            return response

            
            
        else:
            self.notification.setText(f"Bad url address. Please enter one of elenta.lt url")




app = QApplication([])

window = Window()

window.show()
app.exec() 