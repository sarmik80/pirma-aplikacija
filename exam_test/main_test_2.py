import os
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow
from designtest import Ui_MainWindow 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.enter_button.clicked.connect(self.start_scraping)

    def start_scraping(self):
        url = self.url_field.text()

        if "https://elenta.lt" not in url:
            self.notification.setText("Invalid URL. Please enter a valid https://elenta.lt URL.")
            return

        data = self.scraped_data(url)
        self.notification.setText("Scraping complete! Wait for the results!")

        if data:
            total_value = self.calculate_total_value(data)
            num_ads = len(data)
            self.found.setText(f"Found {num_ads} ads with a total value of {total_value:.2f} EUR")

            try:
               
                script_directory = os.path.dirname(os.path.abspath(__file__))

                
                csv_file_path = os.path.join(script_directory, "data.csv")

                
                with open(csv_file_path, "w", newline= "", encoding= "utf8") as csvfile:
                    fieldnames = ["title", "price"]
                    writer = csv.DictWriter(csvfile, fieldnames= fieldnames, delimiter= ";")
                    writer.writeheader()
                    writer.writerows(data)

            except Exception as e:
                print("Error writing to CSV:", e) 

    def calculate_total_value(self, data):
        total = 0
        for listing in data:
            try:
                
                price_str = listing['price'].replace(" ", "").replace("€", "")
                price = float(price_str)
                total += price
            except ValueError:
                pass  
        return total

    def scraped_data(self, url):
        response = []
        try:
            
            options = webdriver.ChromeOptions() 
            driver = webdriver.Chrome(options=options) 
            driver.get(url)

            while True:
                
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.units-list li'))
                )

                html = BeautifulSoup(driver.page_source, "html.parser")
                data = html.select('.units-list li')

                self.notification.setText(f"Scraping: {driver.current_url}") 

                for listing in data:
                    title = listing.select_one('a.ad-hyperlink')
                    title = title.text if title else ""
                    price = listing.select_one('.price-box')
                    price = price.text if price else "0"
                    response.append({"title": title, "price": price})

                
                next_page = driver.find_elements(By.CSS_SELECTOR, '.pagerNextPage a') 
                sleep(1)

                if next_page:
                    next_page[0].click()  
                else:
                    break 

            driver.quit()  
            return response

        except Exception as e:
            self.notification.setText(f"Error: {e}")
            return []

app = QApplication([])
window = Window()
window.show()
app.exec()