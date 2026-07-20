import copy

from PySide6.QtCore import Qt
import PySide6.QtWidgets as qt
import load
import search
ALL_POKEMON,ALL_MOVES,ALL_ABILITIES = load.load_data()
ABILITY_NAMES = []
for i in ALL_ABILITIES:
    ABILITY_NAMES.append(ALL_ABILITIES[i]["name"])
class SearchTab(qt.QWidget):
    def __init__(self):
        super().__init__()
        left = qt.QVBoxLayout()
        right = qt.QVBoxLayout()

        self.stats = dict()
        statsInputs = qt.QFormLayout()
        for stat_name in ["HP", "Attack", "Defense", "Special-Attack", "Special-Defense", "Speed"]:
            stat_value = qt.QLineEdit()
            stat_value.setMaxLength(3)
            mode_choice = qt.QComboBox()
            mode_choice.addItems(["Minimum","Exact","Maximum"])

            self.stats[stat_name] = {"value": stat_value, "mode": mode_choice}

            stat = qt.QHBoxLayout()
            stat.addWidget(stat_value)
            stat.addWidget(mode_choice)
            statsInputs.addRow(stat_name,stat)
        left.addLayout(statsInputs)


        details = qt.QHBoxLayout()

        self.game = qt.QComboBox()
        self.game.addItems(["Champions","Scarlet-Violet"])
        details.addWidget(self.game)

        self.ability = qt.QLineEdit()
        self.ability.setPlaceholderText("Ability")
        details.addWidget(self.ability)
        self.ability_completer = qt.QCompleter(ABILITY_NAMES)
        self.ability_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ability.setCompleter(self.ability_completer)


        self.type1 = qt.QLineEdit()
        self.type1.setPlaceholderText("Type 1")
        self.type2 = qt.QLineEdit()
        self.type2.setPlaceholderText("Type 2")
        details.addWidget(self.type1)
        details.addWidget(self.type2)

        left.addLayout(details)
        left.addWidget(qt.QLabel("Moves"))
        self.moves = qt.QListWidget()
        left.addWidget(self.moves)

        self.searchbutton = qt.QPushButton("Search")
        left.addWidget(self.searchbutton)


        right.addWidget(qt.QLabel("Results"))
        self.results_list = qt.QListWidget()
        right.addWidget(self.results_list)

        FullLayout = qt.QHBoxLayout()
        FullLayout.addLayout(left)
        FullLayout.addLayout(right)

        self.setLayout(FullLayout)
        self.searchbutton.clicked.connect(self.Search)


    def Search(self):
        if self.ability.text() in ABILITY_NAMES:
            validpokemon = search.search_ability(self.ability.text(),ALL_POKEMON)
        else:
            validpokemon = copy.deepcopy(ALL_POKEMON)
        queue = dict()
        for i in self.stats:
            try:
                value = int(self.stats[i]["value"].text())
                if value < 1:
                    continue
                queue[i.lower()] = {"value": value, "mode": self.stats[i]["mode"].currentText().lower()}
            except Exception:
                continue
        self.results_list.clear()
        results = search.search_stats(queue,validpokemon)
        for i in results:
            self.results_list.addItem(i)

class OtherTab(qt.QWidget):
    def __init__ (self):
        super().__init__()
        weird = qt.QVBoxLayout()
        weird.addWidget(qt.QPushButton("Nothing"))
        self.setLayout(weird)


class MainWindow(qt.QMainWindow):
    def __init__(self):
        super().__init__()

        tabs = qt.QTabWidget()
        tabs.addTab(SearchTab(), "Search")
        tabs.addTab(OtherTab(), "Pokémon")

        self.setCentralWidget(tabs)
        self.setWindowTitle("PokéFind")
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)

if __name__ == "__main__":
    app = qt.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
