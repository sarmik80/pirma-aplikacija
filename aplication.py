from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow) :
    def __init__(self):
        super(). __init__()
        self.setupUi(self)

    def handleClick(self):
        print("Paspaudimias ivyko")

app = QApplication([])

window = Window()

window.show()

app.exec()
        