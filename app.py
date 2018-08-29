from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        for i in range(0, 3):
            button = QPushButton('btn {}'.format(i))
            layout.addWidget(button)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
