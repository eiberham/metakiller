from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QWidget, QMessageBox, QListWidget
from pathlib import Path
import sys
import os
import glob

from archive import *

class Metakiller(QMainWindow):
    def __init__(self):
        super().__init__()

        icon = QIcon()
        icon.addPixmap(QPixmap('knife.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(icon)
        self.resize(300, 150)

        self.archives = []

        title = "Metakiller"
        self.setWindowTitle(title) 

        self.button = QPushButton('Search Image Folder')
        self.button.clicked.connect(self.get_image_file)

        self.label = QLabel('Pick the source folder, images will be automatically optimized')


        self.list = QListWidget()

        wid = QWidget(self)
        self.setCentralWidget(wid)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.list)

        wid.setLayout(layout)
    
    def get_image_file(self):
        home = str(Path.home())
        dirname = QFileDialog.getExistingDirectory(self, "Select directory", home, QFileDialog.ShowDirsOnly)
        if dirname == '': 
            return

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
            image.save('./output/' + file, optimize=True, quality=30)

            head, tail = os.path.split('./output/' + file)
            self.archives.append(Archive(tail, head))
            
        for arch in self.archives:
            self.list.addItem(str(arch.get_name()) + ' stale size: ' + str(arch.get_stale_size()) + ' size: ' + str(arch.get_size()) + 'bytes')

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