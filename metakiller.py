from PIL import Image
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QWidget, QMessageBox
from pathlib import Path
import sys
import os
import glob

from archive import *
from graph import *


class Metakiller(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Metakiller, self).__init__(*args, **kwargs)

        icon = QIcon()
        icon.addPixmap(QPixmap('knife.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(icon)
        self.setIconSize(QtCore.QSize(72, 72))
        self.resize(300, 350)
        self.setAcceptDrops(True)

        self.archives = []

        title = "Metakiller"
        self.setWindowTitle(title) 

        self.button = QPushButton('Search Image Folder')
        self.button.clicked.connect(self.get_image_file)

        self.label = QLabel('Pick the source folder, images will be automatically optimized')

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.widget.setLayout(self.layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        dirname = None
        for url in event.mimeData().urls():
            dirname = url.toLocalFile()

        files = self.filter_files(dirname)

        self.optimize_files(files)

    def filter_files(self, dirname):
        if dirname == '': 
            return

        os.chdir(dirname)

        files = []
        extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif']
        
        for ext in extensions:
            files.extend(glob.glob(ext))

        return files
    
    def get_image_file(self):
        home = str(Path.home())
        dirname = QFileDialog.getExistingDirectory(self, "Select directory", home, QFileDialog.ShowDirsOnly)

        files = self.filter_files(dirname)
        
        self.optimize_files(files)
        

    def optimize_files(self, files):
        if not os.path.exists('output'):
            os.makedirs('output')

        for file in files:
            head, tail = os.path.split(file)
            archive = Archive(tail, head)
    
            self.archives.append(archive)

            image = Image.open(file)
            image.save('./output/' + file, optimize=True, quality=30)
            archive.set_size(os.path.getsize('./output/' + file))

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Done')
        msg.setText('Images were optimized')
        msg.setInformativeText('Please look within the output folder')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.build_graph()

    def build_graph(self):
        graph_dictionary = {}
        for arch in self.archives:
            graph_dictionary[arch.get_name()] = {
                'stale' : arch.get_stale_size(),
                'optimized' : arch.get_size()
            }

        self.graph = BarGraph().draw(graph_dictionary)
        self.layout.addWidget(self.graph)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    metakiller = Metakiller()
    metakiller.show()
    sys.exit(app.exec_())