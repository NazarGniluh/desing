from PyQt5.QtWidgets import *


app = QApplication([])

app.setStyleSheet(
    """
    QPushButton:hover {
        background-color:white;
    }
        QWidget {
            background:rgb(255, 255, 128);
        }
        
        QPushButton
        {
            background-color:rgba(255, 255, 128, .5);
            
            font-size: 15px;
            color: black;
            border-style: solid;
            border-width: 1px;
            border-color: black;
            border-radius: 5px;
            
        
           
            
        }
                
    """)

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
windows7 = QLabel("НОМЕРОГРАМ")


mono1 = QPushButton("ПАПКА")
mono2 = QPushButton("АБОНЕНТ")
mono3 = QPushButton("НОМЕР")
mono4 = QPushButton("РІДНИЙ")
mono5 = QPushButton("КОЛЄГА")
mono6 = QPushButton("БАТЬКІВЩИНА")

text = QTextEdit()


Mon = QVBoxLayout()
Mon.addWidget(mono1)
Mon.addWidget(text)

mainLine.addLayout(Mon)


Mon1 = QVBoxLayout()
Mon1.addWidget(windows7)
Non = QHBoxLayout()
Non.addWidget(mono2)
Non.addWidget(mono3)
Non.addWidget(mono4)
Non.addWidget(mono5)
Non.addWidget(mono6)

Mon1.addLayout(Non)

mainLine.addLayout(Mon1)




window.setLayout(mainLine)


window.show()
app.exec()