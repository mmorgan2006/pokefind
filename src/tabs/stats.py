from PySide6.QtCore import Qt
import PySide6.QtWidgets as qt
import statcalc
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
        fullLayout = qt.QHBoxLayout()
        leftLayout = qt.QVBoxLayout()


        row = 1
        statsgrid = qt.QGridLayout()
        statsgrid.addWidget(qt.QLabel("Base"),0,1)
        statsgrid.addWidget(qt.QLabel("IVs"),0,2)
        statsgrid.addWidget(qt.QLabel("EVs"),0,3)
        self.stats = {}
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            stat_value = qt.QLineEdit()
            iv_value = qt.QLineEdit()
            ev_value = qt.QLineEdit()
            stat_value.setMaxLength(3)
            iv_value.setMaxLength(2)
            ev_value.setMaxLength(3)

            self.stats[stat] = {"base": stat_value, "iv": iv_value, "ev": ev_value}

            statsgrid.addWidget(qt.QLabel(stat),row,0)
            statsgrid.addWidget(stat_value,row,1)
            statsgrid.addWidget(iv_value,row,2)
            statsgrid.addWidget(ev_value,row,3)
            row += 1
        leftLayout.addLayout(statsgrid)
        self.level_value = qt.QLineEdit()
        self.level_value.setPlaceholderText("Level")
        leftLayout.addWidget(self.level_value)

        self.nature_field = qt.QLineEdit()
        self.nature_field.setPlaceholderText("Nature")
        self.nature_completer = qt.QCompleter(list(dict.keys(natures)))
        self.nature_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.nature_field.setCompleter(self.nature_completer)
        leftLayout.addWidget(self.nature_field)

        rightlayout = qt.QVBoxLayout()
        rightlayout.addWidget(qt.QLabel("Results"))
        self.results_list = qt.QListWidget()
        self.results_list.setFixedWidth(200)
        rightlayout.addWidget(self.results_list)

        self.calculate_button = qt.QPushButton("Calculate")
        leftLayout.addWidget(self.calculate_button)
        leftLayout.addStretch()
        fullLayout.addLayout(leftLayout)


        fullLayout.addStretch()
        self.setLayout(fullLayout)
        self.calculate_button.clicked.connect(self.Calculate)



    def Calculate(self):
        try:
            level = int(self.level_value.text())
        except Exception:
            self.level_value.setText("50")
            level = 50
        if self.nature_field.text().lower() in list(dict.keys(natures)):
            nature = self.nature_field.text().lower()
        else:
            nature = "serious"
        pokemon = {"level": level, "nature": nature,"stats": {}}
        for stat in self.stats:
            for i in self.stats[stat]:
                if stat not in pokemon["stats"]:
                    pokemon["stats"][stat] = {"base": 0,"iv": 0,"ev": 0}
                try:
                    value = int(self.stats[stat][i].text())
                    if value < 1:
                        pokemon["stats"][stat][i] = 0
                    else:
                        pokemon["stats"][stat][i] = value
                except Exception:
                    continue
        stats = statcalc.calc3(pokemon)

class CalcChamp(qt.QWidget):
    def __init__(self):
        super().__init__()
