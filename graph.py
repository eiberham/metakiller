from pyqtgraph import PlotWidget, plot, BarGraphItem
import numpy as np

class PlotGraph(PlotWidget):
    def __init__(self):
        PlotWidget.__init__(self)
        self.x = None
        self.y = None
    
    def plot(self, x, y):
        self.plot(x, y)


class BarGraph(PlotWidget):
    def __init__(self):
        PlotWidget.__init__(self)
    
    def draw(self):
        item = BarGraphItem(x=np.linspace(0, 20, num=20), height=np.arange(20), width=0.3, brush='r')
        win = plot()
        win.addItem(item)
        return win
