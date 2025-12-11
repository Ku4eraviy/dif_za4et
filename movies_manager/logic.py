import json
import os
from typing import List


def load_movies(path: str) -> list[dict]:
    """Загрузка списка фильмов из JSON-файла."""
    path = os.path.join(path, "movies.json")
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Ошибка")




def save_movies(path: str, movies: list[dict]) -> None:

    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(movies, file, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError ("Ошибка")

def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    """Добавление нового фильма в список."""
    title = input("Введите название фильма: ")
    try:
        movies.append({"title": title, "year": year})
        return movies
    except ValueError:
        return []


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    """Отметить фильм как просмотренный."""
    pass


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    """Поиск всех фильмов указанного года."""
    pass

