from PySide2 import QtWidgets, QtCore
from functools import partial


class Calculatrice(QtWidgets.QWidget):

    _BTN_TEXT_PLUS = '+'
    _BTN_TEXT_MOINS = '-'
    _BTN_TEXT_FOIS = 'X'
    _BTN_TEXT_DIVIS = '/'
    _BTN_TEXT_C = 'C'
    _BTN_TEXT_EQ = '='
    _BTN_TEXT_POINT = '.'

    def __init__(self):
        super().__init__()

        self.btns_nb = []
        """:type: list[QtWidgets.QPushButton]"""

        self.setWindowTitle('Ma super caltos')

        self._setup_ui()
        self._setupConnection()

    def _setup_ui(self):
        grid_layout = QtWidgets.QGridLayout(self)

        self.le_operation = QtWidgets.QLineEdit()
        grid_layout.addWidget(self.le_operation, 0, 0, 1, 4)

        self.le_result = QtWidgets.QLineEdit()
        grid_layout.addWidget(self.le_result, 1, 0, 1, 4)

        self.btns_nb = []
        i = 0
        for j in range(3, 6):
            for k in range(0, 3):
                button = QtWidgets.QPushButton('%s' % (i))
                i += 1
                self.btns_nb.append(button)
                grid_layout.addWidget(button, j, k, 1, 1)

        self.btn_point = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_POINT)
        grid_layout.addWidget(self.btn_point, 6, 2, 1, 1)

        self.btn_plus = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_PLUS)
        grid_layout.addWidget(self.btn_plus, 5, 3, 1, 1)

        self.btn_moins = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_MOINS)
        grid_layout.addWidget(self.btn_moins, 4, 3, 1, 1)

        self.btn_fois = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_FOIS)
        grid_layout.addWidget(self.btn_fois, 3, 3, 1, 1)

        self.btn_divis = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_DIVIS)
        grid_layout.addWidget(self.btn_divis, 2, 3, 1, 1)

        self.btn_egal = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_EQ)
        grid_layout.addWidget(self.btn_egal, 6, 3, 1, 1)

        self.btn_c = QtWidgets.QPushButton(Calculatrice._BTN_TEXT_C)
        grid_layout.addWidget(self.btn_c, 2, 0, 1, 1)

        for i in range(grid_layout.count()):
            item = grid_layout.itemAt(i).widget()
            if isinstance(item, QtWidgets.QPushButton):
                item.setFixedSize(64, 64)

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
