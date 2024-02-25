import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon,QAction


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('뚜.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        exitAction2 = QAction(QIcon('뚜.jpg'), 'Exit', self)
        exitAction2.setShortcut('Ctrl+W')
        exitAction2.setStatusTip('Exit application')
        exitAction2.triggered.connect(qApp.quit)
        exitAction3 = QAction(QIcon('뚜.jpg'), 'Exit', self)
        exitAction3.setShortcut('Ctrl+T')
        exitAction3.setStatusTip('Exit application')
        exitAction3.triggered.connect(qApp.quit)
        exitAction4 = QAction(QIcon('뚜.jpg'), 'Exit', self)
        exitAction4.setShortcut('Ctrl+C')
        exitAction4.setStatusTip('Exit application')
        exitAction4.triggered.connect(qApp.quit)

        menu=self.menuBar()
        menu.setNativeMenuBar(False)
        filemenu = menu.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(exitAction2)
        filemenu.addAction(exitAction3)
        filemenu.addAction(exitAction4)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addWidget(menu)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())