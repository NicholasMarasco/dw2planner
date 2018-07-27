import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QDesktopWidget,
    QGridLayout,
    QLineEdit,
    QLabel,
    QComboBox,
    QSpacerItem,
)
from PyQt5 import QtGui

def startUI():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = UI_MainWindow(window)
    window.show()
    sys.exit(app.exec_())

class UI_MainWindow(QWidget):

    def __init__(self, MainWindow):
        super().__init__()
        self.initUI(MainWindow)

    def initUI(self, MainWindow):

        # Labels
        startLabel = QLabel('Start')
        endLabel   = QLabel('End')

        # ComboBox fields
        startBox = QComboBox(self)
        startBox.addItem("Agumon")
        startBox.addItem("Greymon")
        endBox = QComboBox(self)
        endBox.addItem("MetalGreymon")
        endBox.addItem("WarGreymon")

        # Grid layout
        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(startLabel, 1, 0)
        grid.addWidget(startBox, 1, 1)

        grid.addWidget(endLabel, 2, 0)
        grid.addWidget(endBox, 2, 1)

        grid.addWidget(QPushButton('Go', self), 3, 0)
        qButton = QPushButton('Quit', self)
        qButton.clicked.connect(QApplication.instance().quit)
        qButton.resize(qButton.sizeHint())
        grid.addWidget(qButton, 4, 0)
        self.setLayout(grid)

        # Window settings
        MainWindow.setWindowTitle("DW2Planner")
        MainWindow.setCentralWidget(self)
        MainWindow.resize(250,100)
        self.center(MainWindow)

    def center(self, MainWindow):
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

if __name__ == '__main__':
    startUI()
