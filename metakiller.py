#init environment: source metakiller/bin/activate
#quit environment: deactivate
#to install PyQt5: pip3 install PyQt5

from PIL import Image
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QVBoxLayout
from pathlib import Path
import sys

class Window(QMainWindow):
    def __init__(self):
        """ image = Image.open('./image.jpg')
        image.save('./image2.jpg') """

        window = QMainWindow()

        title = "Tile of window"
    
        # set the title 
        window.setWindowTitle(title) 

        home = str(Path.home())

        label = QLabel('Pick the source folder of all the images you want to optimize')

        filename = QFileDialog.getOpenFileName(self,"Open Image", home, "Image Files (*.png *.jpg *.bmp)")

        layout = QVBoxLayout()

        layout.addWidget(label)
        layout.addWidget(filename)

        # setting  the geometry of window 
        window.setGeometry(0, 0, 500, 300) 

        window.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())