import PySide6.QtWidgets as qt
import load
import search
ALL_POKEMON,ALL_MOVES,ALL_ABILITIES = load.load_data()


class SearchTab(qt.QWidget):
    def __init__(self):
        super().__init__()

        left = qt.QVBoxLayout()
        right = qt.QVBoxLayout()

        self.stats = dict()
        statsInputs = qt.QFormLayout()
        for stat_name in ["HP", "Attack", "Defense", "Special-Attack", "Special-Defense", "Speed"]:
            stat_value = qt.QLineEdit()
            mode_choice = qt.QComboBox()
            mode_choice.addItems(["Minimum","Exact","Maximum"])

            self.stats[stat_name] = {"value": stat_value, "mode": mode_choice}

            stat = qt.QHBoxLayout()
            stat.addWidget(stat_value)
            stat.addWidget(mode_choice)
            statsInputs.addRow(stat_name,stat)
        left.addLayout(statsInputs)

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
        results = search.search_stats(queue)
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
        tabs.addTab(OtherTab(), "Tab")

        self.setCentralWidget(tabs)
        self.setWindowTitle("Pokefind")

if __name__ == "__main__":
    app = qt.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
