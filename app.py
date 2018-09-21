from PySide2 import QtWidgets, QtGui
from functools import partial

from custom_ui.calculette import Ui_form_calculatrice


class Calculatrice(Ui_form_calculatrice, QtWidgets.QWidget):


    def __init__(self):
        super().__init__()

        self.btns_nb = []
        """:type: list[QtWidgets.QPushButton]"""

        self.setupUi(self)
        self._custom_setup_ui()
        self._setup_keyboard_shortcuts()
        self._setupConnection()

    def _setup_keyboard_shortcuts(self):
        for btn in range(10):
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self._btnNombrePressed, str(btn)))

        QtWidgets.QShortcut(
            QtGui.QKeySequence('+'),
            self,
            partial(self._btnOperationPressed, str(self.btn_plus.text())))
        QtWidgets.QShortcut(
            QtGui.QKeySequence('-'),
            self,
            partial(self._btnOperationPressed, str(self.btn_moins.text())))
        QtWidgets.QShortcut(
            QtGui.QKeySequence('*'),
            self,
            partial(self._btnOperationPressed, str(self.btn_fois.text())))
        QtWidgets.QShortcut(
            QtGui.QKeySequence('/'),
            self,
            partial(self._btnOperationPressed, str(self.btn_divis.text())))

        QtWidgets.QShortcut(
            QtGui.QKeySequence('enter'),
            self,
            self._calculOperation)

        QtWidgets.QShortcut(
            QtGui.QKeySequence('del'),
            self,
            self._supprimerResultat)

        QtWidgets.QShortcut(
            QtGui.QKeySequence('esc'),
            self,
            self.close)

    def _custom_setup_ui(self):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton) and widget.text().isdigit():
                self.btns_nb.append(widget)

    def _setupConnection(self):
        self.btn_egal.clicked.connect(self._calculOperation)
        self.btn_c.clicked.connect(self._supprimerResultat)

        for btn in self.btns_nb:
            btn.clicked.connect(partial(self._btnNombrePressed, str(btn.text())))

        self.btn_plus.clicked.connect(partial(self._btnOperationPressed, str(self.btn_plus.text())))
        self.btn_moins.clicked.connect(partial(self._btnOperationPressed, str(self.btn_moins.text())))
        self.btn_divis.clicked.connect(partial(self._btnOperationPressed, str(self.btn_divis.text())))
        self.btn_fois.clicked.connect(partial(self._btnOperationPressed, str(self.btn_fois.text())))

    def _btnNombrePressed(self, bouton: str):
        """Fonction activee quand l'utilisateur appuie sur un numero (0-9)"""

        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_result.text())

        if resultat == '0':
            # Si le resultat est egal a 0 on met le nombre du bouton
            # que l'utilisateur a presse dans le LineEdit resultat
            self.le_result.setText(bouton)
        else:
            # Si le resultat contient autre chose que zero,
            # On ajoute le texte du bouton a celui dans le LineEdit resultat
            self.le_result.setText(resultat + bouton)

    def _btnOperationPressed(self, operation: str):
        """
        Fonction activee quand l'utilisateur appuie sur
        une touche d'operation (+, -, /, *)
        """

        # On recupere le texte dans le LineEdit operation
        operationText = str(self.le_operation.text())
        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_result.text())

        # On additionne l'operation en cours avec le texte dans le resultat
        # et on ajoute a la fin le signe de l'operation qu'on a choisie
        self.le_operation.setText(operationText + resultat + operation)
        # On reset le texte du LineEdit resultat
        self.le_result.setText('0')

    def _supprimerResultat(self):
        """On reset le texte des deux LineEdit"""

        self.le_result.setText('0')
        self.le_operation.setText('')

    def _calculOperation(self):
        """On calcule le resultat de l'operation en cours (quand l'utilisateur appuie sur egal)"""

        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.le_result.text())

        # On ajoute le nombre actuel dans le LineEdit resultat
        # au LineEdit operation
        self.le_operation.setText(self.le_operation.text() + resultat)

        # On evalue le resultat de l'operation
        resultatOperation = eval(str(self.le_operation.text()))

        # On met le resultat final dans le LineEdit resultat
        self.le_result.setText(str(resultatOperation))


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Calculatrice()
    window.show()
    app.exec_()
