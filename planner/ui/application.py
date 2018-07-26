import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QDesktopWidget,
    QAction,
    QMenu,
    QGridLayout,
    QLineEdit,
    QTextEdit,
    QLabel,
    qApp
)
from PyQt5.QtGui import QFont, QIcon

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
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # Grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        qButton = QPushButton('Quit', self)
        qButton.clicked.connect(QApplication.instance().quit)
        qButton.resize(qButton.sizeHint())
        grid.addWidget(qButton, 7, 0)
        grid.addWidget(QPushButton('Button', self), 6, 0)
        self.setLayout(grid)

        # Window settings
        MainWindow.resize(800,600)
        self.center(MainWindow)
        MainWindow.setWindowTitle("Centered")
        MainWindow.setCentralWidget(self)

    def center(self, MainWindow):
        qr = MainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

if __name__ == '__main__':
    startUI()
