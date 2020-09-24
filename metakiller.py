from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QWidget, QMessageBox
from pathlib import Path
import sys
import os
import glob
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from archive import *
from graph import *


class Metakiller(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Metakiller, self).__init__(*args, **kwargs)

        icon = QIcon()
        icon.addPixmap(QPixmap('knife.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(icon)
        self.resize(300, 350)

        self.archives = []

        title = "Metakiller"
        self.setWindowTitle(title) 

        self.button = QPushButton('Search Image Folder')
        self.button.clicked.connect(self.get_image_file)

        self.label = QLabel('Pick the source folder, images will be automatically optimized')
        

        """ hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45] """

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # self.layout.addWidget(self.graph)

        # plot data: x, y values
        # self.plotWidget.plot(hour, temperature)

        self.widget.setLayout(self.layout)
    
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
            head, tail = os.path.split(file)
            print(tail, ' ', head)
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

        self.get_graph_dictionary()

    def get_graph_dictionary(self):
        graph = {}
        for arch in self.archives:
            graph[arch.get_name()] = {
                'a' : arch.get_stale_size(),
                'b' : arch.get_size()
            }
        print(graph)
        self.graph = BarGraph().draw(graph)
        self.layout.addWidget(self.graph)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    metakiller = Metakiller()
    metakiller.show()
    sys.exit(app.exec_())