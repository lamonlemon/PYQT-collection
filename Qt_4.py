import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
new=True
class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setWindowIcon(QIcon('notepad.png'))
        self.textEdit.textChanged.connect(self.text_changed)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        saveNewFile = QAction(QIcon('open.png'), 'Save', self)
        saveNewFile.setShortcut('Ctrl+Shift+S')
        saveNewFile.setStatusTip('Save as a New')
        saveNewFile.triggered.connect(self.save_new)

        saveFile = QAction(QIcon('open.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save')
        saveFile.triggered.connect(self.save_new)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveNewFile)
        fileMenu.addAction(saveFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 740, 500)
        self.show()

    def text_changed(self):
        global new
        new=False
        print("hi")

    def showDialog(self):
        global fname
        global new
        if new==False:
            reply=QMessageBox.question(self, 'Notepad', 'Are you sure to save?',QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Yes)
            if reply==QMessageBox.Yes:
                text = self.textEdit.toPlainText()
                save = QFileDialog.getSaveFileName(self, 'Save as a new', './','Text files (*.txt)\nPython files (*.py)\nAll files (*.*)')
                if save[0]:
                    with open(save[0], mode="w+")as s:
                        s.write(text)
                elif reply==QMessageBox.No:
                    fname = QFileDialog.getOpenFileName(self, 'Open file', './')
                    new=True
                    if fname[0]:
                        f = open(fname[0], 'r+')
                        with f:
                            data = f.read()
                            self.textEdit.setText(data)
        else:
            fname = QFileDialog.getOpenFileName(self, 'Open file', './')
            new=True
            if fname[0]:
                f = open(fname[0], 'r+')
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
    def save_new(self):
        text = self.textEdit.toPlainText()
        if new==True:
            save = QFileDialog.getSaveFileName(self, 'Save as a new', './','Text files (*.txt)\nPython files (*.py)\nAll files (*.*)')
            if save[0]:
                with open(save[0], mode="w+")as s:
                    s.write(text)

    def save(self):
        text = self.textEdit.toPlainText()
        if new==False:
            print(new)
            s=open(fname[0],'w+')
            with s:
                s.write(text)
        else:
            save = QFileDialog.getSaveFileName(self, 'Save as a new', './','Text files (*.txt)\nPython files (*.py)\nAll files (*.*)')
            if save[0]:
                with open(save[0], mode="w+")as s:
                    s.write(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())