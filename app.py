from PySide2 import QtWidgets, QtCore


class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Signaux')

        self._layout = QtWidgets.QVBoxLayout(self)
        button = QtWidgets.QPushButton('Clique ici !')
        button.clicked.connect(self._on_button_click)
        button.released.connect(self._on_button_released)

        self._layout.addWidget(button)

    def _on_button_click(self):
        button = QtWidgets.QPushButton('coucou')
        self._layout.addWidget(button)

    def _on_button_released(self):
        print('c\'est bon !')


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainFrame()
    window.show()
    app.exec_()
