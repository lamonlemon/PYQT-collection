import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt5.QtCore import QTimer

class MoleGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("두더지 잡기 게임")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.score_label = QLabel("점수: 0", self)
        self.score_label.setGeometry(10, 10, 100, 30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_mole)

        self.mole_button = QPushButton("두더지", self)
        self.mole_button.setGeometry(150, 150, 100, 50)
        self.mole_button.clicked.connect(self.hit_mole)

        self.score = 0
        self.update_score()

    def show_mole(self):
        x = random.randint(0, self.width() - self.mole_button.width())
        y = random.randint(0, self.height() - self.mole_button.height())
        self.mole_button.move(x, y)
        self.mole_button.show()

    def hit_mole(self):
        self.score += 1
        self.update_score()
        self.mole_button.hide()

    def update_score(self):
        self.score_label.setText(f"점수: {self.score}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MoleGame()
    game.show()

    # 두더지를 나타내는 타이머를 시작합니다.
    game.timer.start(1000)

    sys.exit(app.exec_())
