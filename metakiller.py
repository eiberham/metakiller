from PIL import Image
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QWidget, QMessageBox
from pathlib import Path
import sys
import os
import glob

class Metakiller(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)

        title = "Tile of window"
        self.setWindowTitle(title) 

        self.button = QPushButton('Search Image')
        self.button.clicked.connect(self.get_image_file)

        self.label = QLabel('Pick the source folder of all the images you want to optimize')

        wid = QWidget(self)
        self.setCentralWidget(wid)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        wid.setLayout(layout)
    
    def get_image_file(self):
        home = str(Path.home())
        dirname = QFileDialog.getExistingDirectory(self, "Select directory", home, QFileDialog.ShowDirsOnly)
        os.chdir(dirname)

        files = []
        extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif']
        
        for ext in extensions:
            files.extend(glob.glob(ext))
        
        self.optimize_files(files)
        

    def optimize_files(self, files):
        if not os.path.exists('output'):
            os.makedirs('output')

        for file in files:
            image = Image.open(file)
            image.save('./output/' + file)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Done')
        msg.setText('Images were optimized')
        msg.setInformativeText('Please look within the output folder')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    metakiller = Metakiller()
    metakiller.show()
    sys.exit(app.exec_())