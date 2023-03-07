import sys
import matplotlib
matplotlib.use('Qt5Agg')

import PyQt6
from PyQt6.QtCore import QSize, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt6.QtWidgets import  QApplication, QMainWindow,QLabel,QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        # self.setCentralWidget(sc)
        RR_label = QLabel("Breath Rate")
        horizontal_layout0  = QVBoxLayout()
        horizontal_layout0.addWidget(RR_label)
        horizontal_layout0.addWidget(sc)

        self.show()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()