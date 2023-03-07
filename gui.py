
import sys
from pathlib import Path
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



import PyQt6
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtCore , QtWidgets
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel,QWidget, QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPalette, QColor
import pyqtgraph as pg
from random import randint



class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

# class MplCanvas(FigureCanvasQTAgg):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Patient Monitor")
        # # self.setFixedSize(QSize(400, 300)) #will create a fixed size window of 400x300 pixels.
        
        self.HR_label = QLabel("Heart Rate", alignment=Qt.AlignmentFlag.AlignHCenter)
        self.HR_label.setObjectName('HR_label')

        self.HR_widget = QLabel("100", alignment=Qt.AlignmentFlag.AlignHCenter)
        self.HR_widget.setObjectName('HR_widget')
        # self.HR_widget.setObjectName("number")

        # HR_widget.setText("2") # to change it later
        # HR_font = self.HR_widget.font()
        # HR_font.setPointSize(30)
        # self.HR_widget.setFont(HR_font)
        # self.HR_widget.setStyleSheet('background-color:blue ; font-size:20px;color:red')

        RR_label = QLabel("Breath Rate", alignment=Qt.AlignmentFlag.AlignHCenter)
        RR_label.setObjectName('RR_label')

        RR_widget = QLabel("24", alignment=Qt.AlignmentFlag.AlignHCenter)
        RR_widget.setObjectName('RR_widget')
        # RR_widget.setObjectName("number")
        # HR_widget.setText("2") # to change it later
        RR_font = RR_widget.font()
        RR_font.setPointSize(30)
        RR_widget.setFont(RR_font)

        ECG_label = QLabel("ECG ", alignment=Qt.AlignmentFlag.AlignHCenter)
        ECG_label.setObjectName('ECG_label')

        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        # toolbar = NavigationToolbar(sc, self)

        # hour = [1,2,3,4,5,6,7,8,9,10]
        # temperature = [30,32,34,32,33,31,29,32,35,45]
        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        # plot data: x, y values
        self.data_line = self.graphWidget.plot(self.x, self.y)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()


        connect_btn = QPushButton("Connect")
        stop_btn = QPushButton("Stop")

############################ Layouts ##################################

        horizontal_layout0  = QHBoxLayout()
        horizontal_layout0.addWidget(self.HR_label)
        horizontal_layout0.addWidget(RR_label)
        widget0=QWidget()
        widget0.setObjectName('widget0')
        widget0.setLayout(horizontal_layout0)


        # Create Horizontal Layout1 (FOR HR and RR)
        horizontal_layout1  = QHBoxLayout()
        horizontal_layout1.addWidget(self.HR_widget)
        horizontal_layout1.addWidget(RR_widget)
        horizontal_layout1.setContentsMargins(0,0,0,0) # for the layout (right , top , left, bottom)
        horizontal_layout1.setSpacing(10) # for widgets inside layout

        # Create Horizontal Layout2 (FOR stop_btn and connect_btn)
        horizontal_layout2  = QHBoxLayout()
        horizontal_layout2.addWidget(connect_btn)
        horizontal_layout2.addWidget(stop_btn)

        # Create Horizontal Layout
        vertical_layout  = QVBoxLayout()
        vertical_layout.addWidget(widget0 )
        vertical_layout.addLayout(horizontal_layout1 )
        vertical_layout.addWidget(ECG_label)
        vertical_layout.addWidget( self.graphWidget)
        # vertical_layout.addWidget(toolbar)
        # vertical_layout.addWidget(sc)
        vertical_layout.addLayout(horizontal_layout2 )


        widget=QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.


app = QtWidgets.QApplication(sys.argv)

qss_file = open('style.qss').read()
app.setStyleSheet(qss_file)

# app.setStyleSheet(Path('style.qss').read_text())


window = MainWindow()
window.show()

app.exec()