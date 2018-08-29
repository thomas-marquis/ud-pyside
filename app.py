from PySide2 import QtWidgets, QtCore


class MyApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout(self)

        progress = QtWidgets.QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(50)
        progress.setTextVisible(False)

        layout.addWidget(progress)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
