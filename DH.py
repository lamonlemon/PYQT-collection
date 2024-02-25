import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import pyttsx3

form_class = uic.loadUiType("DH.ui")[0]
index = 0        
text_list = []

def get_text_list(text):
    list = []
    index = 0
    first = index
    last = index
    text2 = text
    text_len = len(text2)
    while index<text_len:
        if text[index] != '.'and text[index] !=  '!'and text[index] !=  '?':
            index+=1
        else:
            last = index
            list.append(text[first:last])
            first = last+1
            index+=1

    if index != last:
        list.append(text[first:index])
        print(text[first:index])
    return list

def speak(list2):
    global index
    if index < len(list2):
        speak_text(list2[index])

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10
        self.setWindowTitle("dictation help")
        self.setWindowIcon(QIcon('dh.png'))

        self.play.clicked.connect(self.play_clicked)
        self.Next.clicked.connect(self.Next_clicked)
        self.load.clicked.connect(self.load_clicked)
        self.show_btn.clicked.connect(self.show_btn_clicked)

    def load_clicked(self):
        global index
        global text_list
        return_text = self.textEdit.toPlainText()
        text_list = get_text_list(return_text)
        self.label.setText(str(index+1))
        self.label_2.setText(str(len(text_list)))
        self.textEdit.clear()

    def play_clicked(self):
        global text_list
        speak(text_list)

    def Next_clicked(self):
        global index
        global text_list
        if index<len(text_list):
            index+=1
        else:
            index = 0
        self.label.setText(str(index+1))

    def show_btn_clicked(self):
        global text_list
        text = ''
        for string in text_list:
            text+=string
        self.textEdit.setText(text)
            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()