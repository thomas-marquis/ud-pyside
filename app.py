from PySide2 import QtWidgets, QtCore


class Calculatrice(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ma super caltos')

        self._setup_ui()

    def _setup_ui(self):
        grid_layout = QtWidgets.QGridLayout(self)

        le_opperation = QtWidgets.QLineEdit()
        grid_layout.addWidget(le_opperation, 0, 0, 1, 4)

        le_result = QtWidgets.QLineEdit()
        grid_layout.addWidget(le_result, 1, 0, 1, 4)

        for i in range(0, 10):
            for j in range(3, 6):
                for k in range(0, 3):
                    button = QtWidgets.QPushButton('{}'.format(i))
                    grid_layout.addWidget(button, j, k, 1, 1)

        btn_point = QtWidgets.QPushButton('.')
        grid_layout.addWidget(btn_point, 6, 2, 1, 1)

        btn_plus = QtWidgets.QPushButton('+')
        grid_layout.addWidget(btn_plus, 5, 3, 1, 1)

        btn_moins = QtWidgets.QPushButton('-')
        grid_layout.addWidget(btn_moins, 4, 3, 1, 1)

        btn_fois = QtWidgets.QPushButton('X')
        grid_layout.addWidget(btn_fois, 3, 3, 1, 1)

        btn_divis = QtWidgets.QPushButton('/')
        grid_layout.addWidget(btn_divis, 2, 3, 1, 1)

        btn_egal = QtWidgets.QPushButton('=')
        grid_layout.addWidget(btn_egal, 6, 3, 1, 1)

        btn_c = QtWidgets.QPushButton('C')
        grid_layout.addWidget(btn_c, 2, 0, 1, 1)

        for i in range(grid_layout.count()):
            item = grid_layout.itemAt(i).widget()
            if isinstance(item, QtWidgets.QPushButton):
                item.setFixedSize(64, 64)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Calculatrice()
    window.show()
    app.exec_()
