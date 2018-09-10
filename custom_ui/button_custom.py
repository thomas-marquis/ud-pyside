from PySide2 import QtWidgets, QtGui

CUSTOM_FONT = QtGui.QFont()
CUSTOM_FONT.setPointSize(24)


class ButtonCutom(QtWidgets.QPushButton):

    def __init__(self, text):
        super().__init__(text)

        self.setFont(CUSTOM_FONT)
        self.setStyleSheet('QPushButton:hover {color: rgb(100, 200, 130);}')

    def enterEvent(self, event: QtGui.QEnterEvent):
        print('--> %s' % self.text())

    def leaveEvent(self, *args, **kwargs):
        print('%s -->' % self.text())
