import json
import os
import logging


chemin_1 = "C:/Users/Willy Durand Wakam/Desktop/Uni/Python/Python/Cine/data/movies.json"

def get_movies():
    with open(chemin_1, "r") as f:
        movies_title = json.load(f)


    movies = [Movie(movie)for movie in movies_title]
    return movies
class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(chemin_1, "r") as f:
           return json.load(f)

    def _write_movies(self, movies):
        with open(chemin_1, "w") as f:
           return json.dump(movies, f, indent=4)


    def add_to_movies(self):
        liste = self._get_movies()

        if self.title not in liste:
            liste.append(self.title)
            self._write_movies(liste)
            return True

        else:
            logging.warning(f"The movie {self.title} already exist")
            return False

    def remove_from_movies(self):
        liste = self._get_movies()

        if self.title in liste:
            liste.remove(self.title)
            self._write_movies(liste)
            return True

        else:
            logging.warning(f"The movie {self.title} does not exist")
            return False

if __name__ == "__main__":
    moviee = get_movies()
    print(moviee)