from PySide2 import QtWidgets, QtCore
from functools import partial

class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Signaux')

        self._layout = QtWidgets.QVBoxLayout(self)
        button = QtWidgets.QPushButton('Clique ici !')
        button.clicked.connect(partial(self._on_button_click, 'premier bouton'))

        button_2 = QtWidgets.QPushButton('un autre bouton')
        button_2.clicked.connect(partial(self._on_button_click, 'deuxième bouton'))

        self._layout.addWidget(button)
        self._layout.addWidget(button_2)

    def _on_button_click(self, text):
        print(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainFrame()
    window.show()
    app.exec_()
