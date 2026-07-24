import PySide6.QtWidgets as qt
from tabs.searchp import SearchTab
from tabs.pokemon import PokemonTab
from tabs.stats import StatCalculator

class MainWindow(qt.QMainWindow):
    def __init__(self):
        super().__init__()

        tabs = qt.QTabWidget()
        tabs.addTab(SearchTab(), "Search")
        tabs.addTab(PokemonTab(), "Pokémon")
        tabs.addTab(StatCalculator(), "Stats")

        self.setCentralWidget(tabs)
        self.setWindowTitle("PokéFind")
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)

if __name__ == "__main__":
    app = qt.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
