
import sys
from pathlib import Path
import matplotlib
from random import randint

from data import get_data

import PyQt5
from PyQt5 import QtWidgets , QtCore ,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph  as pg

# import PyQt6
# from PyQt6.QtCore import QSize, Qt
# from PyQt6 import QtCore , QtWidgets
# from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel,QWidget, QVBoxLayout,QHBoxLayout
# from PyQt6.QtGui import QPalette, QColor
# import pyqtgraph as pg

# import PySide6 
# from  PySide6.QtWidgets import QGraphicsDropShadowEffect



# # importing libraries
# from PyQt5.QtWidgets import * 
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import * 
# from PyQt5.QtCore import * 




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
        

        ############### 1) HR ###############
        self.HR_label = QLabel("Heart Rate", alignment=Qt.AlignmentFlag.AlignHCenter)
        self.HR_label.setObjectName('HR_label')

        self.HR_widget = QLabel("100", alignment=Qt.AlignmentFlag.AlignHCenter)
        self.HR_widget.setObjectName('HR_widget')
        HR_shadow = QGraphicsDropShadowEffect()  
        HR_shadow.setColor(Qt.white)
        HR_shadow.setYOffset(0.5)
        HR_shadow.setXOffset(0.5)
        HR_shadow.setBlurRadius(5)
        # self.HR_widget.setGraphicsEffect(HR_shadow)

        HR_layout  = QVBoxLayout()
        HR_layout.addWidget(self.HR_label)
        HR_layout.addWidget(self.HR_widget)

        widget1 =QWidget()
        widget1.setLayout(HR_layout)
        widget1.setObjectName("widget1")


        ############### 2) RR ###############

        RR_label = QLabel("Breath Rate", alignment=Qt.AlignmentFlag.AlignHCenter)
        RR_label.setObjectName('RR_label')

        RR_widget = QLabel("24", alignment=Qt.AlignmentFlag.AlignHCenter)
        RR_widget.setObjectName('RR_widget')
        RR_shadow = QGraphicsDropShadowEffect()  
        RR_shadow.setColor(Qt.white)
        RR_shadow.setYOffset(0.5)
        RR_shadow.setXOffset(0.5)
        RR_shadow.setBlurRadius(5)
        # RR_widget.setGraphicsEffect(RR_shadow)
        # HR_widget.setText("2") # to change it later
        RR_layout  = QVBoxLayout()
        RR_layout.addWidget(RR_label)
        RR_layout.addWidget(RR_widget)
                
        widget2 =QWidget()
        widget2.setLayout(RR_layout)
        widget2.setObjectName("widget2")

        ############### 3) ECG ###############

        ECG_label = QLabel("ECG ", alignment=Qt.AlignmentFlag.AlignHCenter)
        ECG_label.setObjectName('ECG_label')


        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.pen = pg.mkPen(color=(255, 238, 99))
        self.data_line = self.graphWidget.plot(self.x, self.y , pen = self.pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        ECG_layout  = QVBoxLayout()
        ECG_layout.addWidget(ECG_label)
        ECG_layout.addWidget(self.graphWidget )
                
        widget3 =QWidget()
        widget3.setLayout(ECG_layout)
        widget3.setObjectName("widget3")

        connect_btn = QPushButton("Connect")
        stop_btn = QPushButton("Stop")

############################ Layouts ##################################

        horizontal_layout_HR_RR  = QHBoxLayout()
        horizontal_layout_HR_RR.addWidget(widget1)
        horizontal_layout_HR_RR.addWidget(widget2)
        horizontal_layout_HR_RR.setContentsMargins(0,0,0,0) # for the layout (right , top , left, bottom)
        horizontal_layout_HR_RR.setSpacing(0) # for widgets inside layout

        # Create Horizontal Layout2 (FOR stop_btn and connect_btn)
        horizontal_layout2  = QHBoxLayout()
        horizontal_layout2.addWidget(connect_btn)
        horizontal_layout2.addWidget(stop_btn)

        # Create Vertical Layout
        vertical_layout  = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout_HR_RR )
        vertical_layout.addWidget(widget3)
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