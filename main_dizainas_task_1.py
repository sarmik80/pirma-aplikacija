from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas_task_1 import Ui_MainWindow

skaiciuotuvas = 0

class Window(QMainWindow, Ui_MainWindow):
    skaiciuotuvas = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.padidinti.clicked.connect(self.padidinimas)
        # self.sumazinti.clicked.connect(self.sumazinimas)


    def padidinimas(self):
        self.skaiciuotuvas += 1
        self.zinute.setText("Padidinote vinetu")

    # def sumazinimas(self):
    #     self.zinute.set.text("Sumazinote vienetu")

app = QApplication([])

window = Window()

window.show()
app.exec()       

                 