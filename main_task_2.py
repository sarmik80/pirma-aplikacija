from PyQt6.QtWidgets import QApplication, QMainWindow
from task_2 import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pateikti.clicked.connect(self.pateikimas)

    def pateikimas(self):

        ivesti_metai = self.gimimo_metai.text()
        # print(ivesti_metai)
        amzius = 2024 - int(ivesti_metai)
        # print(amzius)
        self.rezultatas.setText(f"Sveiki, jūsų vardas {self.vardas.text()} {self.pavarde.text()}, Jums yra {amzius} metai")
        

app = QApplication([])

window = Window()

window.show()
app.exec()