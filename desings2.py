from PyQt5.QtWidgets import *


app = QApplication([])


window = QWidget()

window.resize(800, 500)
mainLine = QHBoxLayout()


Non = QHBoxLayout()

windows1 = QLabel("ПАПКА")
windows2 = QLabel("АБОНЕНТ")
windows3 = QLabel("НОМЕР")
windows4 = QLabel("РІДНИЙ")
windows5 = QLabel("КОЛЄГА")
windows6 = QLabel("БАТЬКІВЩИНА")


mono1 = QPushButton("ПАПКА")
mono2 = QPushButton("АБОНЕНТ")
mono3 = QPushButton("НОМЕР")
mono4 = QPushButton("РІДНИЙ")
mono5 = QPushButton("КОЛЄГА")
mono6 = QPushButton("БАТЬКІВЩИНА")

text = QTextEdit()
kom = QLineEdit()

Mon = QVBoxLayout()
Mon.addWidget(mono1)
Mon.addWidget(text)

mainLine.addLayout(Mon)



Mon1 = QVBoxLayout()
mainLine.addLayout(Mon1)


window.setLayout(mainLine)


window.show()
app.exec()