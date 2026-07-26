from PySide6.QtCore import Qt
import PySide6.QtWidgets as qt
import search
import copy
from load import ALL_POKEMON,MOVE_NAMES,ABILITY_NAMES,TYPELIST
class SearchTab(qt.QWidget):
    def __init__(self):
        super().__init__()
        left = qt.QVBoxLayout()
        right = qt.QVBoxLayout()

        # STATS
        self.stats = dict()
        statsInputs = qt.QFormLayout()
        for stat_name in ["HP", "Attack", "Defense", "Special-Attack", "Special-Defense", "Speed"]:
            stat_value = qt.QLineEdit()
            stat_value.setMaxLength(3)
            stat_value.setFixedWidth(40)
            mode_choice = qt.QComboBox()
            mode_choice.addItems(["Minimum","Exact","Maximum"])
            mode_choice.setFixedWidth(130)

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

        # ABILITY
        self.ability = qt.QLineEdit()
        self.ability.setPlaceholderText("Ability")
        details.addWidget(self.ability)
        self.ability_completer = qt.QCompleter(ABILITY_NAMES) #type: ignore
        self.ability_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ability.setCompleter(self.ability_completer)
        left.addLayout(details)

        # TYPES
        details = qt.QHBoxLayout()
        self.type1 = qt.QLineEdit()
        self.type1.setPlaceholderText("Type 1")
        self.type2 = qt.QLineEdit()
        self.type2.setPlaceholderText("Type 2")
        self.type_completer = qt.QCompleter(TYPELIST)
        self.type_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.type1.setCompleter(self.type_completer)
        self.type2.setCompleter(self.type_completer)
        details.addWidget(self.type1)
        details.addWidget(self.type2)
        left.addLayout(details)

        # MOVES
        details = qt.QHBoxLayout()

        self.move_completer = qt.QCompleter(MOVE_NAMES) #type: ignore
        self.move_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.move_field = qt.QLineEdit()
        self.move_field.setPlaceholderText("Add Move")
        self.move_field.setCompleter(self.move_completer)
        details.addWidget(self.move_field)

        self.add_move = qt.QPushButton("+")
        self.add_move.setFixedWidth(30)
        details.addWidget(self.add_move)

        self.clear_moves = qt.QPushButton("Clear Moves")
        details.addWidget(self.clear_moves)

        left.addLayout(details)
        self.moves = qt.QListWidget()
        self.moves.setFixedHeight(125)
        self.moves_list = []

        left.addWidget(self.moves)

        self.searchbutton = qt.QPushButton("Search")
        left.addWidget(self.searchbutton)


        right.addWidget(qt.QLabel("Results"))
        self.results_list = qt.QListWidget()
        self.results_list.setFixedWidth(200)
        right.addWidget(self.results_list)

        FullLayout = qt.QHBoxLayout()
        FullLayout.addLayout(left)
        FullLayout.addLayout(right)

        self.setLayout(FullLayout)
        self.searchbutton.clicked.connect(self.Search)
        self.add_move.clicked.connect(self.AddMove)
        self.clear_moves.clicked.connect(self.ClearMoves)
        self.results_list.itemDoubleClicked.connect(self.ClickResult)
        self.moves.itemClicked.connect(self.ClickMove)


    def Search(self):
        game = self.game.currentText()
        validpokemon = copy.deepcopy(ALL_POKEMON)
        if self.ability.text() in ABILITY_NAMES:
            validpokemon = search.search_ability(self.ability.text(),validpokemon)
        else:
            self.ability.setText("")
        if len(self.moves_list) > 0:
            for m in self.moves_list:
                validpokemon = search.search_move(m, validpokemon, game)
        if self.type1.text() in TYPELIST:
            validpokemon = search.search_type(self.type1.text().lower(),validpokemon)
        else:
            self.type1.setText("")
        if self.type2.text() in TYPELIST:
            if self.type2.text() != self.type1.text():
                validpokemon = search.search_type(self.type2.text().lower(),validpokemon)
        else:
            self.type2.setText("")
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

    def AddMove(self):
        move = self.move_field.text()
        self.move_field.setText("")
        if len(self.moves_list) < 4:
            if move in MOVE_NAMES and move not in self.moves_list:
                self.moves_list.append(move)
                self.moves.addItem(move)

    def ClearMoves(self):
        self.moves.clear()
        self.moves_list = []
    def ClickResult(self,item):
        tabs = self.parentWidget().parentWidget() #type: ignore

        tabs.setCurrentIndex(1) #type: ignore
        tabs.widget(1).load_pokemon(item.text()) #type: ignore
    def ClickMove(self, item):
        row = self.moves.row(item)
        self.moves.takeItem(row)
        self.moves_list.remove(item.text())
