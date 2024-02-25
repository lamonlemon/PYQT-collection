import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('webEngineViewTest.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #WebEngineView의 시그널
        self.webEngineView.urlChanged.connect(self.urlChangedFunction)
        self.webEngineView.loadProgress.connect(self.printLoading)
        self.webEngineView.loadFinished.connect(self.printLoadFinished)
        self.webEngineView.urlChanged.connect(self.urlChangedFunction)

        #버튼들에 기능을 연결
        self.btn_setUrl.clicked.connect(self.urlGo)
        self.btn_back.clicked.connect(self.btnBackFunc)
        self.btn_forward.clicked.connect(self.btnForwardFunc)
        self.btn_reload.clicked.connect(self.btnRelaodFunc)

    def urlChangedFunction(self) :
        self.line_url.setText(self.webEngineView.url().toString())
        print("Url Changed")
    def printLoadStart(self) : print("Start Loading")
    def printLoading(self) : print("Loading")
    def printLoadFinished(self) : print("Load Finished")

    #버튼을 눌렀을 때 실행될 함수들
    def urlGo(self) :
        self.webEngineView.load(QUrl(self.line_url.text()))

    def btnBackFunc(self) :
        self.webEngineView.back()

    def btnForwardFunc(self) :
        self.webEngineView.forward()

    def btnRelaodFunc(self) :
        self.webEngineView.reload()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec()