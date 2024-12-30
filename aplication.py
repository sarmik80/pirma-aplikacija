from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow) :
    def __init__(self):
        super(). __init__()
        self.setupUi(self)

        self.pirmas_mygtukas.clicked.connect(self.handleClick())
        self.antras_mygtukas.clicked.connect(self.handleClick())
        self.trecias_mygtukas.clicked.connect(self.handleClick())

    def handleClick(self):
        print("Paspaudimias ivyko")

app = QApplication([])

window = Window()

window.show()

app.exec()
        