from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLable, QBoxLayout
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(
    Question('Государственный язык Бразилия', 'Португалия', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(
    Question('Государственный язык Бразилия', 'Португалия', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(
    Question('Государственный язык Бразилия', 'Португалия', 'Английский', 'Испанский', 'Бразильский'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Meno Card')

btn_OK = QPushButton('Ответить')
ib_Question = QLable('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответа')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLauoyt(layout_ans2)
layout_ans1.addLauoyt(layout_ans2)

layout_ans1.addLauoyt(layout_ans2)
layout_ans1.addLauoyt(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QBoxLayout()
layout_line1 = QBoxLayout()
layout_line1 = QBoxLayout()

layout_card.addLauoyt(layout_ans1, stretch = 2)
layout_card.addLauoyt(layout_ans2, stretch = 8)
layout-card.addStretch(1)
layout_card.addLauoyt(layout_ans3, stretch = 1)
layout-card.addStretch(1)
layout-card.addStretch(5)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.Alignment | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QBoxLayout('Результат теста')
lb_Result = QLable

layout_card = QVBoxLayout()

layout_card.addLauoyt(layout_line1, stretch=2)
layout_card.addLauoyt(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLauoyt(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)

answer[1].setText(q.wrong1)
answer[2].setText(q.wrong2)
answer[3].setText(q.wrong3lb_)

def next_question():
    window.total += 1
    print('Статистика \n Всего вопросов', window.total, '\n Правильных ответов:', window.score)

window = QWidget()
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(200, 200)
window.setLayout(layout_card)
window.show()
app.exec()