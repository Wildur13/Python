from PySide2 import QtWidgets
from movie import get_movies
from movie import Movie


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.setup_cine()
        self.populate_movies()
        self.setup_connections()
        self.setup_css()

    def setup_cine(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.edit = QtWidgets.QLineEdit()
        self.btn_ajout = QtWidgets.QPushButton("Add Movie")
        self.movies_liste = QtWidgets.QListWidget()
        self.movies_liste.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_retrait = QtWidgets.QPushButton("Remove Movie(s)")

        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.btn_ajout)
        self.layout.addWidget(self.movies_liste)
        self.layout.addWidget(self.btn_retrait)

    def setup_connections(self):
        self.btn_ajout.clicked.connect(self.add_movie)
        self.btn_retrait.clicked.connect(self.remove_movies)
        self.edit.returnPressed.connect(self.add_movie)

    def setup_css(self):
        self.setStyleSheet("""
            background-color: gray;
            color: white;
        """)
        self.edit.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.movies_liste.setStyleSheet("""
            background-color: white;
            color: blue;
            font-weight: bold;
            font-family: 'Montserrat', sans-serrif;
        """)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_movies = QtWidgets.QListWidgetItem(movie.title)
            self.movies_liste.addItem(lw_movies)


    def add_movie(self):
        movie_title = self.edit.text()

        if not movie_title:
            return False

        movie = Movie(title=movie_title)
        result = movie.add_to_movies()
        if result:
            self.movies_liste.addItem(movie.title)
            
            
        self.edit.setText("")

    def remove_movies(self):
        for selected_item in self.movies_liste.selectedItems():
            movie = Movie(selected_item.text())
            movie.remove_from_movies()
            self.movies_liste.takeItem(self.movies_liste.row(selected_item))



app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()