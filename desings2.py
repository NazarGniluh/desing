from PyQt5.QtWidgets import *


app = QApplication([])


window = QWidget()

window.resize(800, 500)
mainLine = QHBoxLayout()



window.setLayout(mainLine)
window.show()
app.exec()