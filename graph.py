from pyqtgraph import PlotWidget, plot, BarGraphItem
import numpy as np

class BarGraph(PlotWidget):
    def __init__(self):
        PlotWidget.__init__(self)
    
    def draw(self, graph_dictionary):
        win = plot()
        length = len(graph_dictionary)
        print(len(graph_dictionary))
        for key in graph_dictionary:
            print(graph_dictionary[key].get('a'))
            print(graph_dictionary[key].get('b'))
            stale = BarGraphItem(x=np.arange(0, length), height=graph_dictionary[key].get('a'), width=0.3, brush='r')
            fixed = BarGraphItem(x=np.arange(0, length), height=graph_dictionary[key].get('b'), width=0.3, brush='b')
            win.addItem(stale)
            win.addItem(fixed)
        return win
