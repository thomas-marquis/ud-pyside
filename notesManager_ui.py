from PySide2 import QtWidgets

from customUi.notesManager import Ui_NotesManager


class NoteManager(QtWidgets.QWidget, Ui_NotesManager):

    def __init__(self):
        super(NoteManager, self).__init__()

        self.setupUi(self)
        self._setup_connections()
        self.show()

    def _setup_connections(self):
        self.create_note_btn.clicked.connect(self._create_note)
        self.notes_list_output.itemClicked.connect(self._display_note)
        self.update_note_btn.clicked.connect(self._update_note)
        self.delete_note_btn.clicked.connect(self._delete_note)

    def _create_note(self):
        print('créer une note')

    def _display_note(self):
        print('afficher la note')

    def _update_note(self):
        print('mettre à jour la note')

    def _delete_note(self):
        print('supprimer la note')

    def _get_notes(self):
        pass


app = QtWidgets.QApplication([])
note_manager = NoteManager()
app.exec_()
