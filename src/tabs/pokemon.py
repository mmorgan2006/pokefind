import PySide6.QtWidgets as qt

class PokemonTab(qt.QWidget):
    def __init__ (self):
        super().__init__()
        weird = qt.QVBoxLayout()
        weird.addWidget(qt.QPushButton("Nothing"))
        self.setLayout(weird)
