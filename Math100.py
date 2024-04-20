import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import random

class MathGame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Prosta Gra Matematyczna')
        self.setGeometry(100, 100, 400, 300)

        # Ustawianie ikony aplikacji
        self.setWindowIcon(QtGui.QIcon('resources/favicon.ico'))

        self.setStyleSheet(
            """
            QWidget {
                background-color: #fefbd8; /* Ustawienie koloru tła całej aplikacji */
                color: #50394c; /* Ustawienie koloru czcionki */
            }
            QPushButton#button-56 {
                background-color: #618685;
                border: 2px solid #111;
                border-radius: 8px;
                color: #fefbd8;
                font-family: "Serif", monospace;
                font-size: 18px;
                height: 48px;
                line-height: 24px;
                padding: 0 25px;
                text-align: center;
                text-decoration: none;
            }
            QPushButton#button-56:hover {
                background-color: #36486b;
            }
            """
        )

        self.score = 100
        self.rounds = 17
        self.round_num = 0

        font = QFont()
        font.setFamily("Serif")
        font.setPointSize(16)

        self.score_label = QLabel(f'Aktualny wynik: {self.score}')
        self.score_label.setFont(font)
        self.round_label = QLabel(f'Runda: {self.round_num + 1}')
        self.round_label.setFont(font)
        self.info_label = QLabel('')
        self.info_label.setFont(font)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.round_label)
        self.layout.addWidget(self.info_label)

        self.setLayout(self.layout)

        self.start_round()

    def start_round(self):
        self.round_num += 1
        self.round_label.setText(f'Runda: {self.round_num}')
        self.info_label.setText('Wybierz liczbę, aby odjąć od wyniku.')

        self.numbers = [random.randint(0, 9) for _ in range(3)]

        self.buttons_layout = QVBoxLayout()
        self.buttons = []

        for number in self.numbers:
            button = QPushButton(f'Odejmij {number}', objectName="button-56")
            button.clicked.connect(self.handle_click)
            self.buttons_layout.addWidget(button)
            self.buttons.append(button)

        self.layout.addLayout(self.buttons_layout)

        # Ustawianie okna na środku ekranu
        screen = QDesktopWidget().screenGeometry()
        x = int((screen.width() - self.width()) / 2)
        y = int((screen.height() - self.height()) / 2)

        self.move(x, y)

    def handle_click(self):
        choice = int(self.sender().text().split(' ')[1])
        self.score -= choice
        self.score_label.setText(f'Aktualny wynik: {self.score}')

        if self.score < 0:
            QMessageBox.about(self, 'Koniec gry', 'Przegrałeś! Twój wynik spadł poniżej zera.')
            self.restart_game()
        elif self.score == 0:
            QMessageBox.about(self, 'Koniec gry', 'Wygrałeś! Udało ci sie zejść do zera.')
            self.restart_game()
        elif self.round_num > self.rounds:
            QMessageBox.about(self, 'Koniec gry', f'Koniec rund. Twój ostateczny wynik: {self.score}')
            self.restart_game()
        else:
            for button in self.buttons:
                button.deleteLater()
            self.start_round()

    def restart_game(self):
        reply = QMessageBox.question(self, 'Restart gry', 'Czy chcesz zagrać ponownie?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.score = 100
            self.round_num = 0
            self.score_label.setText(f'Aktualny wynik: {self.score}')
            self.round_label.setText(f'Runda: {self.round_num + 1}')
            for i in reversed(range(self.buttons_layout.count())):
                self.buttons_layout.itemAt(i).widget().setParent(None)
            self.start_round()
        else:
            self.close()

def main():
    # Ustawianie nowych opcji skalowania
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    game = MathGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
