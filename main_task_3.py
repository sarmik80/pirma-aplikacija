from PyQt6.QtWidgets import QApplication, QMainWindow
from task_3 import Ui_MainWindow

import mysql.connector

# try :
#     # Prisijungimas prie serverio:
#     cnx = mysql.connector.connect(
#         host="127.0.0.1",
#         port=3306,
#         user="root",
#         password="",
#         database="app")
    
# except :
#     # print(e)
#     print("Prisijungimo klaida")



class Window (QMainWindow, Ui_MainWindow) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.enter_button.clicked.connect(self.data_entered)

    def data_entered(self):

        entered_email = self.email_result.text()
        entered_psw = self.psw_result.text()
        set_email = "admin@vilniuscoding.lt"
        set_psw ="123456"

        if set_email == entered_email and entered_psw == set_psw :
            self.notification.setText(f"Sveikiname sėkmingai prisijungus")

        elif entered_email == "" or entered_psw == "" :
            self.notification.setText(f"Negavome jokių duomenų, bandykite dar kartą")

        else:
             self.notification.setText(f"Neteisingi prisijungimo duomenys")    


app = QApplication([])

window = Window()

window.show()
app.exec()

