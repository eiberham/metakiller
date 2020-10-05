from pyqtgraph import PlotWidget, plot, BarGraphItem, PlotWindow, ScatterPlotItem, TextItem
import pyqtgraph as pg
import numpy as np
import math

class BarGraph(PlotWidget):
    def __init__(self):
        PlotWidget.__init__(self, title='Summary')
        pg.setConfigOption('background', 'w')
    
    def draw(self, graph_dictionary):
        self.win = plot()
        self.win.setTitle('Summary')
        xAxisNames = [ (list(graph_dictionary).index(v), v) for v in list(graph_dictionary.keys()) ]

        old = []
        new = []
        for key in graph_dictionary:
            old.append(graph_dictionary[key].get('stale'))
            new.append(graph_dictionary[key].get('optimized'))
        stale = BarGraphItem(x=range(0, len(old)), height=old, width=0.3, brush='r')
        fixed = BarGraphItem(x=range(0, len(new)), pen=pg.mkPen(None), brush='b', name='enhanced', height=new, width=0.3)

        self.win.addItem(stale)
        self.win.addItem(fixed)

        for index, value in enumerate(old):     # outcome e.g.: 0, 2220
            percentage = new[index] * 100 / value
            text = TextItem(text=str(math.ceil(percentage)) + '%', color='#000', anchor=(0,0), angle=0)
            text.setPos(index, value)
            self.win.addItem(text)

        self.win.getPlotItem().getAxis('bottom').setTicks([ xAxisNames ])
        self.win.getPlotItem().getAxis('bottom').setTicksAngle(45)
        return self.win