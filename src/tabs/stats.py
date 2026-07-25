import PySide6.QtWidgets as qt
import statcalc
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
        leftLayout = qt.QGridLayout()
        leftLayout.addWidget(qt.QLabel("Base"),0,1)
        leftLayout.addWidget(qt.QLabel("IVs"),0,2)
        leftLayout.addWidget(qt.QLabel("EVs"),0,3)

        row = 1
        self.stats = {}
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            stat_value = qt.QLineEdit()
            iv_value = qt.QLineEdit()
            ev_value = qt.QLineEdit()
            stat_value.setMaxLength(3)
            iv_value.setMaxLength(2)
            ev_value.setMaxLength(3)

            self.stats[stat] = {"base": stat_value, "iv": iv_value, "ev": ev_value}

            leftLayout.addWidget(qt.QLabel(stat),row,0)
            leftLayout.addWidget(stat_value,row,1)
            leftLayout.addWidget(iv_value,row,2)
            leftLayout.addWidget(ev_value,row,3)
            row += 1
        fullLayout.addLayout(leftLayout)

        self.calculate_button = qt.QPushButton("Calculate")
        fullLayout.addWidget(self.calculate_button)

        fullLayout.addStretch()
        self.setLayout(fullLayout)
        self.calculate_button.clicked.connect(self.Calculate)
    def Calculate(self):
        pokemon = {"level": 78, "nature": "quirky","stats": {}}
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
        print(pokemon)
        statcalc.calc3(pokemon)

class CalcChamp(qt.QWidget):
    def __init__(self):
        super().__init__()
