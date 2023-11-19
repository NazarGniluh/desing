from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import os

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

text = QListWidget()


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

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


class WorkPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filename = None

    def load(self):
        ImagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(ImagePath)


    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800, 600, Qt.KeepAspectRatio)
        windows7.setPixmap(pixel)

    def rotate_clor(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()


    def rotate_clor2(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()


    def black(self):
        self.image = self.image.convert("L")
        self.showImage()

    def Blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.showImage()


    def cont(self):
        self.image = self.image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        self.showImage()

workwithphotos = WorkPhoto()



def open_folder():
    workwithphotos.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(workwithphotos.folder)
    text.clear()
    text.addItems(files)


def showChosenImage():
    workwithphotos.filename = text.currentItem().text()
    workwithphotos.load()
    workwithphotos.showImage()



mono6.clicked.connect(workwithphotos.cont)
mono5.clicked.connect(workwithphotos.Blur)
mono4.clicked.connect(workwithphotos.black)
mono3.clicked.connect(workwithphotos.rotate_clor2)
mono2.clicked.connect(workwithphotos.rotate_clor)
text.currentRowChanged.connect(showChosenImage)
mono1.clicked.connect(open_folder)
window.setLayout(mainLine)
window.show()
app.exec()