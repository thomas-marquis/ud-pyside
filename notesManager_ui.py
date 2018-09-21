from PySide2 import QtWidgets

from customUi.notesManager import Ui_NotesManager


class NoteManager(QtWidgets.QWidget, Ui_NotesManager):

    def __init__(self):
        super(NoteManager, self).__init__()

        self.setupUi(self)
        self.show()


app = QtWidgets.QApplication([])
note_manager = NoteManager()
app.exec_()
