        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)