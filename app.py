from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        button = QPushButton('grand bouton')
        layout.addWidget(button, 0, 0, 1, 3)

        for i in range(1, 3):
            for j in range(0, 3):
                button = QPushButton('{}, {}'.format(i, j))
                layout.addWidget(button, i, j, 1, 1)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
