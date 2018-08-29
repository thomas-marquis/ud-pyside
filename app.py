from PySide2 import QtWidgets


class MyApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout(self)

        lw_demo = QtWidgets.QListWidget(self)
        for i in range(0, 10):
            lw_demo.addItem('nouvel item {}'.format(i))
            lw_demo.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        layout.addWidget(lw_demo)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
