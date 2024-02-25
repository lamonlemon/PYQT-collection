from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from notepad_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.windows = []

        self.action_W.triggered.connect(self.add_window)  # 새 창(W)
        self.action_O.triggered.connect(self.open_file)  # 열기(O)
        self.action_S.triggered.connect(self.save_file)  # 저장(S)

    def add_window(self):  # 새 창(W)
        add_window = MainWindow()
        self.windows.append(add_window)
        add_window.show()

    def open_file(self):  # 열기(O)
        file_name = QFileDialog.getOpenFileName(self)
        if file_name[0]:
            with open(file_name[0], encoding='UTF-8') as f:
                text = f.read()
            self.plainTextEdit.setPlainText(text)

    def save_file(self):  # 저장(S)
        file_name = QFileDialog.getSaveFileName(self)
        if file_name[0]:
            text = self.plainTextEdit.toPlainText()
            with open(file_name[0], 'w', encoding='UTF-8') as f:
                f.write(text)



app = QApplication()
window = MainWindow()
window.show()
app.exec_()
