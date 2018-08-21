from PySide2.QtWidgets import QApplication, QPushButton, QWidget


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        btn_hello = QPushButton('Hello !', self)
        btn_bye = QPushButton('Bye !', self)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
