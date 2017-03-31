import numpy as np
import pandas as pd
from bokeh.embed import components
from bokeh.io import show
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models import HoverTool
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.plotting import figure


TOOLS = 'box_zoom,pan,save,hover,resize,reset,tap,wheel_zoom'

class ChartManager():
    def __init__(self):
        x = np.linspace(-np.pi, np.pi, 201)
        sin = np.sin(x)

        self.fig = figure(width=1200, height=600, tools=TOOLS)
        hover = self.fig.select(dict(type=HoverTool))
        hover.tooltips = [("Series", "@line_name"), ("x", "@x"), ("y", "@y")]
        hover.mode = 'mouse'

        source = ColumnDataSource(pd.DataFrame({'x': x, 'y': sin, 'line_name': "sin"}))

        self.fig.line('x', 'y', source=source, alpha=0.5, line_width=2, legend="sin")
        self.fig.circle('x', 'y', source=source, size=6, legend="sin")



    def getLineAsDiv(self):
        script, div = components(self.fig)
        return script, div


if __name__ == '__main__':
    c = ChartManager()
    show(c.fig)
