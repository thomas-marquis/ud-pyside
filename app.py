from PySide2 import QtWidgets, QtCore


class MyApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout(self)

        checkbox = QtWidgets.QCheckBox('ceci est une checkbox')
        checkbox.setCheckState(QtCore.Qt.Checked)

        print(checkbox.checkState())

        layout.addWidget(checkbox)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
