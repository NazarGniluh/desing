from PIL import Image, ImageFilter, ImageEnhance
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
windows2 = QLabel("ЛІВО")
windows3 = QLabel("ПРАВО")
windows4 = QLabel("ЧОРНИЙ")
windows5 = QLabel("РОЗМИТТЯ")
windows6 = QLabel("РІЗКІСТЬ")
windows7 = QLabel("НОМЕРОГРАМ")
windows8 = QLabel("СТИСНЕННЯ")
windows9 = QLabel("КОНТУР")
windows10 = QLabel("НАСИЧЕНІСТЬ")
windows11 = QLabel("ЗГЛАДЖУЄ")
windows12 = QLabel("ДЕТАЛІЗАЦІЯ")
windows13 = QLabel("РЕБЕР")
windows14 = QLabel("НАЗАД")


mono1 = QPushButton("ПАПКА")
mono2 = QPushButton("ЛІВО")
mono3 = QPushButton("ПРАВО")
mono4 = QPushButton("ЧОРНИЙ")
mono5 = QPushButton("РОЗМИТТЯ")
mono6 = QPushButton("РІЗКІСТЬ")
mono7 = QPushButton("СТИСНЕННЯ")
mono8 = QPushButton("КОНТУР")
mono9 = QPushButton("НАСИЧЕНІСТЬ")
mono10 = QPushButton("ЗГЛАДЖУЄ")
mono11 = QPushButton("ДЕТАЛІЗАЦІЯ")
mono12 = QPushButton("РЕБЕР")
mono13 = QPushButton("НАЗАД")


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
Non.addWidget(mono7)

Mon1.addLayout(Non)

mainLine.addLayout(Mon1)

NOn2 = QHBoxLayout()
NOn2.addWidget(mono8)
NOn2.addWidget(mono9)
NOn2.addWidget(mono10)
NOn2.addWidget(mono11)
NOn2.addWidget(mono12)
NOn2.addWidget(mono13)

Mon1.addLayout(NOn2)
mainLine.addLayout(NOn2)
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


    def stis(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.showImage()

    def kontr(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.showImage()

    def Enctic(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.5)
        self.showImage()

    def Smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.showImage()

    def Detail(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.showImage()

    def Edge(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.showImage()

    def reset_filters(self, factor):
        if self.image:
            
            self.load()
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



mono13.clicked.connect(workwithphotos.reset_filters)
mono12.clicked.connect(workwithphotos.Edge)
mono11.clicked.connect(workwithphotos.Detail)
mono10.clicked.connect(workwithphotos.Smooth)
mono9.clicked.connect(workwithphotos.Enctic)
mono8.clicked.connect(workwithphotos.kontr)
mono7.clicked.connect(workwithphotos.stis)
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