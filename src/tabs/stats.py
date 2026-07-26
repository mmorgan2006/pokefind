from PySide6.QtCore import Qt
import PySide6.QtWidgets as qt
import statcalc
import utils
natures = statcalc.natures
class StatCalculator(qt.QWidget):
    def __init__(self):
        super().__init__()
        layout = qt.QVBoxLayout()
        tabs = qt.QTabWidget()
        tabs.addTab(Calc3(), "Gen-3")
        tabs.addTab(CalcChamp(), "Champions")
        layout.addWidget(tabs)
        self.setLayout(layout)
        self.setWindowTitle("PokéFind")
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)



class Calc3(qt.QWidget):
    def __init__(self):
        super().__init__()
        fullLayout = qt.QVBoxLayout()
        top = qt.QHBoxLayout()
        bottom = qt.QVBoxLayout()


        #STATS
        row = 1
        statsgrid = qt.QGridLayout()
        statsgrid.addWidget(qt.QLabel("Base"),0,1,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        statsgrid.addWidget(qt.QLabel("IVs"),0,2,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        statsgrid.addWidget(qt.QLabel("EVs"),0,3,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        self.stats = {}
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            name = utils.format_stat(stat)
            stat_value = qt.QLineEdit()
            iv_value = qt.QLineEdit()
            ev_value = qt.QLineEdit()
            stat_value.setMaxLength(3)
            iv_value.setMaxLength(2)
            ev_value.setMaxLength(3)

            self.stats[stat] = {"base": stat_value, "iv": iv_value, "ev": ev_value}

            statsgrid.addWidget(qt.QLabel(name),row,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
            statsgrid.addWidget(stat_value,row,1)
            statsgrid.addWidget(iv_value,row,2)
            statsgrid.addWidget(ev_value,row,3)
            row += 1
        top.addLayout(statsgrid)


        details = qt.QHBoxLayout()
        #LEVEL
        self.level_value = qt.QLineEdit()
        self.level_value.setPlaceholderText("Level")
        details.addWidget(self.level_value)

        #NATURE
        self.nature_field = qt.QLineEdit()
        self.nature_field.setPlaceholderText("Nature")
        self.nature_completer = qt.QCompleter(list(dict.keys(natures)))
        self.nature_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.nature_field.setCompleter(self.nature_completer)
        details.addWidget(self.nature_field)

        naturesgrid = qt.QGridLayout()
        naturesgrid.addWidget(qt.QLabel("-Attack"),0,1,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Defense"),0,2,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Sp. Atk"),0,3,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Sp. Def"),0,4,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Speed"),0,5,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)

        naturesgrid.addWidget(qt.QLabel("+Attack"),1,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Defense"),2,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Sp. Atk"),3,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Sp. Def"),4,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Speed"),5,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

        statnames = ["attack","defense","special-attack","special-defense","speed"]
        for i in natures:
            row = statnames.index(natures[i][0]) + 1
            column = statnames.index(natures[i][1]) + 1
            naturebutton = qt.QPushButton(i.title())
            naturebutton.clicked.connect(lambda checked=False, name=i: self.nature_field.setText(name))
            naturesgrid.addWidget(naturebutton,row,column)
        bottom.addLayout(naturesgrid)

        #RESULTS
        results = qt.QVBoxLayout()
        text = qt.QLabel("Results")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        results.addWidget(text)
        self.results_list = qt.QListWidget()
        self.results_list.setFixedWidth(100)
        results.addWidget(self.results_list)
        top.addLayout(results)

        self.calculate_button = qt.QPushButton("Calculate")
        details.addWidget(self.calculate_button)

        bottom.addLayout(details)
        #leftLayout.addStretch()
        fullLayout.addLayout(top)
        fullLayout.addLayout(bottom)

        #fullLayout.addStretch()
        self.setLayout(fullLayout)
        self.calculate_button.clicked.connect(self.Calculate)



    def Calculate(self):
        try:
            level = int(self.level_value.text())
        except Exception:
            self.level_value.setText("50")
            level = 50
        if self.nature_field.text() in list(dict.keys(natures)):
            nature = self.nature_field.text().lower()
        else:
            nature = "serious"
            self.nature_field.setText("")


        if level < 1:
            level = 1
            self.level_value.setText("1")

        pokemon = {"level": level, "nature": nature,"stats": {}}
        for stat in self.stats:
            for i in self.stats[stat]:
                if stat not in pokemon["stats"]:
                    pokemon["stats"][stat] = {"base": 0,"iv": 0,"ev": 0}
                try:
                    value = int(self.stats[stat][i].text())
                except Exception:
                    value = 0
                if i == "base":
                    value = max(value, 1)
                    self.stats[stat][i].setText(str(value))
                if i == "iv":
                    value = utils.clamp(value,0,31)
                    self.stats[stat][i].setText(str(value))
                if i == "ev":
                    value = utils.clamp(value,0,252)
                    self.stats[stat][i].setText(str(value))
                pokemon["stats"][stat][i] = value

        stats = statcalc.calc3(pokemon)
        self.results_list.clear()
        for stat in stats:
            stat_name = utils.format_stat(stat)
            self.results_list.addItem(f"{stat_name}: {stats[stat]}")


class CalcChamp(qt.QWidget):
    def __init__(self):
        super().__init__()
        fullLayout = qt.QVBoxLayout()
        top = qt.QHBoxLayout()
        bottom = qt.QVBoxLayout()


        #STATS
        row = 1
        statsgrid = qt.QGridLayout()
        statsgrid.addWidget(qt.QLabel("Base"),0,1,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        statsgrid.addWidget(qt.QLabel("Stat Points"),0,2,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        self.stats = {}
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            name = utils.format_stat(stat)
            stat_value = qt.QLineEdit()
            ev_value = qt.QLineEdit()
            stat_value.setMaxLength(3)
            ev_value.setMaxLength(2)

            self.stats[stat] = {"base": stat_value, "points": ev_value}

            statsgrid.addWidget(qt.QLabel(name),row,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
            statsgrid.addWidget(stat_value,row,1)
            statsgrid.addWidget(ev_value,row,2)
            row += 1
        top.addLayout(statsgrid)


        details = qt.QHBoxLayout()

        #NATURE
        self.nature_field = qt.QLineEdit()
        self.nature_field.setPlaceholderText("Nature")
        self.nature_completer = qt.QCompleter(list(dict.keys(natures)))
        self.nature_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.nature_field.setCompleter(self.nature_completer)
        details.addWidget(self.nature_field)

        naturesgrid = qt.QGridLayout()
        naturesgrid.addWidget(qt.QLabel("-Attack"),0,1,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Defense"),0,2,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Sp. Atk"),0,3,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Sp. Def"),0,4,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        naturesgrid.addWidget(qt.QLabel("-Speed"),0,5,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)

        naturesgrid.addWidget(qt.QLabel("+Attack"),1,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Defense"),2,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Sp. Atk"),3,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Sp. Def"),4,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        naturesgrid.addWidget(qt.QLabel("+Speed"),5,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

        statnames = ["attack","defense","special-attack","special-defense","speed"]
        for i in natures:
            if i in ["hardy", "docile", "bashful", "quirky"]:
                continue
            row = statnames.index(natures[i][0]) + 1
            column = statnames.index(natures[i][1]) + 1
            if i == "serious":
                row, column = 1,1
            naturebutton = qt.QPushButton(i.title())
            naturebutton.clicked.connect(lambda checked=False, name=i: self.nature_field.setText(name))
            naturesgrid.addWidget(naturebutton,row,column)
        bottom.addLayout(naturesgrid)

        #RESULTS
        results = qt.QVBoxLayout()
        text = qt.QLabel("Results")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        results.addWidget(text)
        self.results_list = qt.QListWidget()
        self.results_list.setFixedWidth(100)
        results.addWidget(self.results_list)
        top.addLayout(results)

        self.calculate_button = qt.QPushButton("Calculate")
        details.addWidget(self.calculate_button)

        bottom.addLayout(details)
        #leftLayout.addStretch()
        fullLayout.addLayout(top)
        fullLayout.addLayout(bottom)

        #fullLayout.addStretch()
        self.setLayout(fullLayout)
        self.calculate_button.clicked.connect(self.Calculate)



    def Calculate(self):
        if self.nature_field.text() in list(dict.keys(natures)):
            nature = self.nature_field.text().lower()
        else:
            nature = "serious"
            self.nature_field.setText("")



        pokemon = {"nature": nature,"stats": {}}
        for stat in self.stats:
            for i in self.stats[stat]:
                if stat not in pokemon["stats"]:
                    pokemon["stats"][stat] = {"base": 0,"points": 0}
                try:
                    value = int(self.stats[stat][i].text())
                except Exception:
                    value = 0
                if i == "base":
                    value = max(value, 1)
                    self.stats[stat][i].setText(str(value))
                if i == "points":
                    value = utils.clamp(value,0,32)
                    self.stats[stat][i].setText(str(value))

                pokemon["stats"][stat][i] = value
        stats = statcalc.calcchamp(pokemon)
        self.results_list.clear()
        for stat in stats:
            stat_name = utils.format_stat(stat)
            self.results_list.addItem(f"{stat_name}: {stats[stat]}")
