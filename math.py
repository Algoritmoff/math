import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from time import time

def show_tripple_plus_minus():
    main_window.start_time = time()
    tripple_plus_minus()
    choice_screen.hide()
    example_screen_1.show()
    line_answer_1.setFocus()

def show_double_mult_1_11():
    main_window.start_time = time()
    double_mult_1_11()
    choice_screen.hide()
    example_screen_2.show()
    line_answer_2.setFocus()

def tripple_plus_minus():
    main_window.end_time = round(time() - main_window.start_time)
    ex_time_1.setText(str(main_window.end_time))
    main_window.start_time = time()
    if line_answer_1.text() == str(main_window.total):
        main_window.score += 1
    else:
        main_window.score -= 1
    lb_score_1.setText(str(main_window.score))
    var = randint(1,2)
    if var == 1:
        x = randint(101,999)
        y = randint(101,999)
        lb_example_1.setText(str(x)+'+'+str(y)+'=')
        main_window.total = x+y
    elif var == 2:
        x = randint(101,999)
        y = randint(101,999)
        lb_example_1.setText(str(x)+'-'+str(y)+'=')
        main_window.total = x-y
    line_answer_1.clear()

def double_mult_1_11():
    if line_answer_2.text() == str(main_window.total):
        main_window.score += 1
    else:
        main_window.score -= 1
    lb_score_2.setText(str(main_window.score))
    var = randint(1,2)
    if var == 1:
        x = randint(12,99)
        y = randint(3,11)
    elif var == 2:
        y = randint(12,99)
        x = randint(3,11)
    main_window.total = x*y
    lb_example_2.setText(str(x)+'*'+str(y)+'=')
    line_answer_2.clear()

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle('Матеша 2.0')
main_window.resize(300, 100)
main_window.move(700, 400)
main_window.total = 0
main_window.score = 1
main_window.start_time = 0
main_window.end_time = 0

font16 = QtGui.QFont()
font16.setPointSize(16)
font24 = QtGui.QFont()
font24.setPointSize(24)

choice_screen = QGroupBox()
lb_choice = QLabel('Выбери вид примеров.')
lb_choice.setFont(font16)
btn_view_1 = QRadioButton('3-х ЗН +- 3-х ЗН')
btn_view_1.setFont(font16)
btn_view_2 = QRadioButton('2-у ЗН * 1-11')
btn_view_2.setFont(font16)
btn_view_3 = QRadioButton('бла бла')
btn_view_3.setFont(font16)
btn_view_4 = QRadioButton('бла бла бла')
btn_view_4.setFont(font16)
choice_main_layout = QVBoxLayout()
choice_row_1 = QHBoxLayout()
choice_row_1.addWidget(btn_view_1, alignment=Qt.AlignCenter)
choice_row_1.addWidget(btn_view_3, alignment=Qt.AlignCenter)
choice_row_2 = QHBoxLayout()
choice_row_2.addWidget(btn_view_2, alignment=Qt.AlignCenter)
choice_row_2.addWidget(btn_view_4, alignment=Qt.AlignCenter)
choice_main_layout.addWidget(lb_choice, alignment=Qt.AlignCenter)
choice_main_layout.addStretch(1)
choice_main_layout.addLayout(choice_row_1)
choice_main_layout.addStretch(1)
choice_main_layout.addLayout(choice_row_2)
choice_screen.setLayout(choice_main_layout)

example_screen_1 = QGroupBox()
lb_score_text_1 = QLabel('Счёт: ')
lb_score_text_1.setFont(font16)
lb_score_1 = QLabel()
lb_score_1.setFont(font16)
lb_time_1 = QLabel('Время: ')
lb_time_1.setFont(font16)
ex_time_1 = QLabel(str(main_window.end_time))
ex_time_1.setFont(font16)
lb_example_1 = QLabel()
lb_example_1.setFont(font24)
line_answer_1 = QLineEdit()
line_answer_1.setFont(font24)
line_answer_1.setPlaceholderText('Сюда пиши ответ')
btn_answer_1 = QPushButton('Ответить')

example_screen_2 = QGroupBox()
lb_score_text_2 = QLabel('Счёт: ')
lb_score_text_2.setFont(font16)
lb_score_2 = QLabel()
lb_score_2.setFont(font16)
lb_view_2 = QLabel('Вид примеров: ')
lb_view_2.setFont(font16)
ex_view_2 = QLabel('2-у ЗН * 1-11')
ex_view_2.setFont(font16)
lb_example_2 = QLabel()
lb_example_2.setFont(font24)
line_answer_2 = QLineEdit()
line_answer_2.setFont(font24)
line_answer_2.setPlaceholderText('Сюда пиши ответ')
btn_answer_2 = QPushButton('Ответить')

main_layout_H = QHBoxLayout()

main_layout_1 = QVBoxLayout()
row_1_1 = QHBoxLayout()
row_1_1.addWidget(lb_score_text_1)
row_1_1.addWidget(lb_score_1)
main_layout_1.addLayout(row_1_1)
row_2_1 = QHBoxLayout()
row_2_1.addWidget(lb_time_1)
row_2_1.addWidget(ex_time_1)
main_layout_1.addLayout(row_2_1)
row_3_1 = QHBoxLayout()
row_3_1.addWidget(lb_example_1,1)
row_3_1.addWidget(line_answer_1,7)
main_layout_1.addLayout(row_3_1)
main_layout_1.addStretch(1)
main_layout_1.addWidget(btn_answer_1)
example_screen_1.setLayout(main_layout_1)

main_layout_2 = QVBoxLayout()
row_1_2 = QHBoxLayout()
row_1_2.addWidget(lb_score_text_2)
row_1_2.addWidget(lb_score_2)
main_layout_2.addLayout(row_1_2)
row_2_2 = QHBoxLayout()
row_2_2.addWidget(lb_view_2)
row_2_2.addWidget(ex_view_2)
main_layout_2.addLayout(row_2_2)
row_3_2 = QHBoxLayout()
row_3_2.addWidget(lb_example_2,1)
row_3_2.addWidget(line_answer_2,7)
main_layout_2.addLayout(row_3_2)
main_layout_2.addStretch(1)
main_layout_2.addWidget(btn_answer_2)
example_screen_2.setLayout(main_layout_2)
main_layout_H.addWidget(choice_screen)
main_layout_H.addWidget(example_screen_1)
main_layout_H.addWidget(example_screen_2)
main_window.setLayout(main_layout_H)
main_window.show()

example_screen_1.hide()
example_screen_2.hide()

btn_view_1.clicked.connect(show_tripple_plus_minus)
btn_view_2.clicked.connect(show_double_mult_1_11)
btn_answer_1.clicked.connect(tripple_plus_minus)
btn_answer_2.clicked.connect(double_mult_1_11)
btn_answer_1.setAutoDefault(True)
btn_answer_2.setAutoDefault(True)
line_answer_1.returnPressed.connect(btn_answer_1.click)
line_answer_2.returnPressed.connect(btn_answer_2.click)
app.exec()
