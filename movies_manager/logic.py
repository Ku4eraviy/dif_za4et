import json
import os
from typing import List,Dict


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
    if not movies:
        new_id = 1
    else:
        new_id = max(movies['id'] for movie in movies) + 1

    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    }

    updated_movies = movies.copy()
    updated_movies.append(new_movie)
    return updated_movies


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    """Отметить фильм как просмотренный."""
    for movie in movies:
        if movie.get('id') == movie_id:
            movie['watched'] = True
            break
    return movies


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    """Поиск всех фильмов указанного года."""
    result = [movie for movie in movies if movie.get['year'] == year]
    return result

