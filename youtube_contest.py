#подключение библиотек

#создание приложения и главного окна
 
#создание виджетов главного окна
 
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 
from random import randint
from PyQt5. QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

def show_win():
    victory_window = QMessageBox()
    victory_window.setText('Поздравляю, вы не под влиянием ктулху, наверное')
    victory_window.exec()

def show_lose():
    victory_window = QMessageBox()
    victory_window.setText('Он под влиянием, увозите его')
    victory_window.exec()

app = QApplication([])
window = QWidget()
window.setWindowTitle('Опрос на влияние ктулху')
window.resize(800, 400)
text = QLabel('Ты кто такой?')
r1_btn = QRadioButton('Ну, человек... наверное')
r1_btn.clicked.connect(show_win)
r2_btn = QRadioButton('Никто и ничто')
r2_btn.clicked.connect(show_lose)
r3_btn = QRadioButton('Не человек')
r3_btn.clicked.connect(show_lose)
r4_btn = QRadioButton('А вы?')
r4_btn.clicked.connect(show_lose)

v_line = QVBoxLayout()
h_lines1 = QHBoxLayout()
h_lines2 = QHBoxLayout()
h_lines3 = QHBoxLayout()
h_lines1.addWidget(text, alignment=Qt.AlignCenter)
h_lines2.addWidget(r1_btn, alignment=Qt.AlignCenter)
h_lines2.addWidget(r2_btn, alignment=Qt.AlignCenter)
h_lines3.addWidget(r3_btn, alignment=Qt.AlignCenter)
h_lines3.addWidget(r4_btn, alignment=Qt.AlignCenter)
v_line.addLayout(h_lines1)
v_line.addLayout(h_lines2)
v_line.addLayout(h_lines3)
window.setLayout(v_line)

window.show()
app.exec()

















































