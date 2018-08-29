from PySide2 import QtWidgets, QtCore


class MyApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QHBoxLayout(self)

        combo_box = QtWidgets.QComboBox()
        combo_box.addItem('delamerde')
        combo_box.addItems(['coucou', 'clic là', 'clic ici plutôt !'])

        combo_box.setCurrentIndex(combo_box.count() - 1)

        combo_box.setItemText(2, 'Nouveau text')

        layout.addWidget(combo_box)

        self.resize(500, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyApplication()
    window.show()
    app.exec_()
