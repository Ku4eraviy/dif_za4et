import json
import os
from typing import List, Dict


def load_movies(path: str) -> List[Dict]:
    full_path = os.path.join(path,)

    if not os.path.exists(full_path):
        print(f"Файл {full_path} не найден.")
        return []

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Некорректный формат данных в файле.")
                return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке файла: {e}")
        return []

def save_movies(path: str, movies: List[Dict]) -> None:
    try:
        with open(os.path.join(path), "w", encoding="utf-8") as file:
            json.dump(movies, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Произошла ошибка при сохранении файлов: {e}")

def add_movie(movies: List[Dict], title: str, year: int) -> List[Dict]:
    if not movies:
        new_id = 1
    else:
        new_id = max(movie["id"] for movie in movies) + 1

    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    }

    updated_movies = movies.copy()
    updated_movies.append(new_movie)
    return updated_movies

def mark_watched(movies: List[Dict], movie_id: int) -> List[Dict]:
    for movie in movies:
        if movie.get("id") == movie_id:
            movie["watched"] = True
            break
    return movies

def find_by_year(movies: List[Dict], year: int) -> List[Dict]:
    result = [movie for movie in movies if movie.get("year") == year]
    return result

def display_movies(movies):
    if len(movies) > 0:
        for movie in movies:
            watched_status = 'Просмотрен' if movie['watched'] else 'Не просмотрен'
            print(f"{movie['id']}. Название: {movie['title']} | Год выпуска: {movie['year']} | Статус: {watched_status}")
    else:
        print("Нет фильмов в каталоге.")