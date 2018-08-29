from PySide2 import QtWidgets


class MyApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        hor_layout = QtWidgets.QHBoxLayout(self)

        for j in range(0, 2):
            vert_layout = QtWidgets.QVBoxLayout(self)

            for i in range(0, 3):
                button = QtWidgets.QPushButton('btn {}'.format(i))
                vert_layout.addWidget(button)

            hor_layout.addLayout(vert_layout)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
