#init environment: source metakiller/bin/activate
#quit environment: deactivate
#to install PyQt5: python3 -m pip install PyQt5
#python -m pip install PyQt5
#brew install pyqt

from PIL import Image
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QWidget
from pathlib import Path
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        """ image = Image.open('./image.jpg')
        image.save('./image2.jpg') """

        self.resize(300, 300)

        title = "Tile of window"
    
        # set the title 
        self.setWindowTitle(title) 

        self.button = QPushButton('Search Image')
        self.button.clicked.connect(self.get_image_file)

        self.label = QLabel('Pick the source folder of all the images you want to optimize')

        wid = QWidget(self)
        self.setCentralWidget(wid)

        layout = QVBoxLayout()

        #layout.addWidget(self.label)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # setting  the geometry of window 
        #window.setGeometry(0, 0, 500, 300) 

        wid.setLayout(layout)
    
    def get_image_file(self):
        home = str(Path.home())
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image", home, "Image Files (*.png *.jpg *.bmp)")

    def optimize():
        print("Hello World")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())