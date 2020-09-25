from pyqtgraph import PlotWidget, plot, BarGraphItem, PlotWindow
import pyqtgraph as pg
import numpy as np

class BarGraph(PlotWidget):
    def __init__(self):
        PlotWidget.__init__(self, title='Summary')
        pg.setConfigOption('background', 'w')
    
    def draw(self, graph_dictionary):
        win = plot()
        win.setTitle('Summary')
        xAxisNames = [ (list(graph_dictionary).index(v), v) for v in list(graph_dictionary.keys()) ]

        oldSize = []
        newSize = []
        for key in graph_dictionary:
            oldSize.append(graph_dictionary[key].get('staleSize'))
            newSize.append(graph_dictionary[key].get('optimizedSize'))
        stale = BarGraphItem(x=range(0, len(oldSize)), height=oldSize, width=0.3, brush='r')
        fixed = BarGraphItem(x=range(0, len(newSize)), pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120), name='scatter', height=newSize, width=0.3)
        
        win.addItem(stale)
        win.addItem(fixed)
        win.getPlotItem().getAxis('bottom').setTicks([ xAxisNames ])
        return win
