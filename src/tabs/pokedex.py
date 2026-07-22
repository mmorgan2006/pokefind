from time import sleep

from PySide6.QtCore import Qt
import PySide6.QtWidgets as qt
from load import SPECIES_NAMES, ALL_POKEMON
import random
class PokedexTab(qt.QWidget):
    def __init__ (self):
        super().__init__()
        self.current_pokedex_widget = None

        top = qt.QHBoxLayout()
        self.search_bar = qt.QLineEdit()
        self.search_bar.setPlaceholderText("Search")
        self.search_completer = qt.QCompleter(SPECIES_NAMES) #type: ignore
        self.search_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.search_bar.setCompleter(self.search_completer)
        top.addWidget(self.search_bar)
        self.search_button = qt.QPushButton("Go")
        top.addWidget(self.search_button)
        self.full_layout = qt.QVBoxLayout()
        self.full_layout.addLayout(top)

        self.setLayout(self.full_layout)

        self.search_button.clicked.connect(lambda: self.load_pokemon(self.search_bar.text()))

        self.load_pokemon(random.choice(list(SPECIES_NAMES)))

    def load_pokemon(self,name):
        self.search_bar.setText("")
        if self.current_pokedex_widget is not None:
            try:
                self.full_layout.removeWidget(self.current_pokedex_widget)
                self.current_pokedex_widget.deleteLater()
            except Exception:
                pass
        new = Pokemon(name)
        self.full_layout.addWidget(new)
        self.current_pokedex_widget = new


class Pokemon(qt.QWidget):
    def __init__(self,name):
        super().__init__()
        key = name.lower().replace(" ","-")
        form = list(dict.keys(ALL_POKEMON[key]["forms"]))
        stats = ALL_POKEMON[key]["forms"][form[0]]["stats"]

        q = qt.QVBoxLayout()
        q.addWidget(qt.QLabel(name))
        for stat in stats:
            q.addWidget(qt.QLabel(f"{stat.title()}: {stats[stat]}"))



        self.setLayout(q)
