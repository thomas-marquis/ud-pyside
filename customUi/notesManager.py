# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/thomas.marquis/workspace/perso/udPyside/customUi\notesManager.ui',
# licensing of 'C:/Users/thomas.marquis/workspace/perso/udPyside/customUi\notesManager.ui' applies.
#
# Created: Fri Sep 21 13:48:04 2018
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NotesManager(object):
    def setupUi(self, NotesManager):
        NotesManager.setObjectName("NotesManager")
        NotesManager.resize(728, 475)
        self.gridLayout = QtWidgets.QGridLayout(NotesManager)
        self.gridLayout.setObjectName("gridLayout")
        self.create_note_btn = QtWidgets.QPushButton(NotesManager)
        self.create_note_btn.setObjectName("create_note_btn")
        self.gridLayout.addWidget(self.create_note_btn, 0, 0, 1, 1)
        self.delete_note_btn = QtWidgets.QPushButton(NotesManager)
        self.delete_note_btn.setObjectName("delete_note_btn")
        self.gridLayout.addWidget(self.delete_note_btn, 0, 1, 1, 1)
        self.edit_note_input = QtWidgets.QTextEdit(NotesManager)
        self.edit_note_input.setObjectName("edit_note_input")
        self.gridLayout.addWidget(self.edit_note_input, 0, 2, 2, 1)
        self.notes_list_output = QtWidgets.QListWidget(NotesManager)
        self.notes_list_output.setObjectName("notes_list_output")
        self.gridLayout.addWidget(self.notes_list_output, 1, 0, 2, 2)
        self.update_note_btn = QtWidgets.QPushButton(NotesManager)
        self.update_note_btn.setObjectName("update_note_btn")
        self.gridLayout.addWidget(self.update_note_btn, 2, 2, 1, 1)

        self.retranslateUi(NotesManager)
        QtCore.QMetaObject.connectSlotsByName(NotesManager)

    def retranslateUi(self, NotesManager):
        NotesManager.setWindowTitle(QtWidgets.QApplication.translate("NotesManager", "Gestionnaire de notes", None, -1))
        self.create_note_btn.setText(QtWidgets.QApplication.translate("NotesManager", "Créer une note", None, -1))
        self.delete_note_btn.setText(QtWidgets.QApplication.translate("NotesManager", "Supprimer la note", None, -1))
        self.update_note_btn.setText(QtWidgets.QApplication.translate("NotesManager", "Mettre à jour le text", None, -1))

