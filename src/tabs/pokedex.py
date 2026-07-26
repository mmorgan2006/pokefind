from time import sleep

from PySide6.QtCore import Qt
import PySide6.QtWidgets as qt
from PySide6.QtGui import QImage, QColor, QPixmap
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
        key = name.lower().replace(" ","-")
        forms = list(dict.keys(ALL_POKEMON[key]["forms"]))
        if len(forms) > 1:
            new = qt.QTabWidget()
            for form in forms:
                new.addTab(Pokemon(key,form), form.title())
        else:
            new = Pokemon(key,key)
        self.full_layout.addWidget(new)
        self.current_pokedex_widget = new


class Pokemon(qt.QWidget):
    def __init__(self,species,form):
        super().__init__()
        color = "#303030"

        species = species.lower().replace(" ","-")
        stats = ALL_POKEMON[species]["forms"][form]["stats"]
        pokemon = qt.QVBoxLayout()
        pokemon.addWidget(qt.QLabel(form.title()))
        stats_layout = qt.QGridLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setHorizontalSpacing(0)
        stats_layout.setVerticalSpacing(0)
        stats_layout.setColumnStretch(0, 1)
        stats_layout.setColumnStretch(1, 1)
        stats_layout.setColumnStretch(2, 10)
        stats_layout.setColumnMinimumWidth(1, 1)

        row_index = 0
        self.bst = 0
        for stat in stats:
            statlabel = qt.QLabel(stat.title())
            statlabel.setFixedHeight(20)
            stats_layout.addWidget(statlabel,row_index,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

            valuelabel = qt.QLabel(f"   {stats[stat]}  ")
            valuelabel.setFixedHeight(20)
            stats_layout.addWidget(valuelabel,row_index,1,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

            bar = qt.QLabel()
            bar.setPixmap(self.set_stat_bar(stats[stat]))
            bar.setFixedHeight(15)
            stats_layout.addWidget(bar,row_index,2,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

            row_index += 1
            self.bst += stats[stat]


        stats_layout.addWidget(qt.QLabel("TOTAL"),row_index,0,alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        stats_layout.addWidget(qt.QLabel(f"   {self.bst}"),row_index,1)

        pokemon.addLayout(stats_layout)


        self.setLayout(pokemon)
    def set_stat_bar(self,value):
        template = QImage("assets/ui/stat_bar.png").convertToFormat(QImage.Format_RGBA8888) #type: ignore

        target_color = QColor("#303030")
        new_color = QColor("#C60913")
        target_color2 = QColor("#1E1E1E")
        new_color2 = QColor("#CE212C")

        for x in range(template.width()):
                for y in range(template.height()):
                    if template.pixelColor(x, y) == target_color:
                        template.setPixelColor(x, y, new_color)
                    if template.pixelColor(x, y) == target_color2:
                        template.setPixelColor(x, y, new_color2)

        width = int(300 * (value / 255))
        template = template.scaled(width,20,Qt.AspectRatioMode.IgnoreAspectRatio,Qt.TransformationMode.SmoothTransformation)
        template = template.copy(0, 0, template.width(), 20)
        template = QPixmap.fromImage(template)
        return template
