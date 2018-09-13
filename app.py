from PySide2 import QtWidgets, QtGui


class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Mon application')


        self.layout = QtWidgets.QHBoxLayout(self)

        self.lw_demo = QtWidgets.QListWidget()
        self.lw_demo.addItems(['premier', 'deuxième', 'troisième'])

        QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Delete'), self, self.lw_demo.clear)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)

        self.layout.addWidget(self.lw_demo)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainFrame()
    window.show()
    app.exec_()
