import PySide6.QtWidgets as qt

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
        for stat in ["hp","attack","defense","special-attack","special-defense","speed"]:
            stat_value = qt.QLineEdit()
            iv_value = qt.QLineEdit()
            ev_value = qt.QLineEdit()
            stat_value.setMaxLength(3)

            leftLayout.addWidget(qt.QLabel(stat),row,0)
            leftLayout.addWidget(stat_value,row,1)
            leftLayout.addWidget(iv_value,row,2)
            leftLayout.addWidget(ev_value,row,3)
            row += 1
        fullLayout.addLayout(leftLayout)
        fullLayout.addStretch()
        self.setLayout(fullLayout)

class CalcChamp(qt.QWidget):
    def __init__(self):
        super().__init__()
