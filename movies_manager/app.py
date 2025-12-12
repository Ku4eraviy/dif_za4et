import json

from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year,display_movies

DATA_FILE = "movies.json"

def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\nКаталог фильмов")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Отметить фильм как просмотренный")
        print("4. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            display_movies(movies)


        elif choice == "2":
            title = input("Введите название фильма: ")
            year_input = input("Введите год выхода фильма: ")
            try:
                year = int(year_input)
                movies = add_movie(movies, title, year)
                print(f"Фильм '{title}' успешно добавлен.")
            except ValueError:
                print("Ошибка: неверный формат года. Попробуйте снова.")

        elif choice == "3":
            movie_id = input("Введите ID фильма, который хотите отметить как просмотренный: ")
            try:
                movie_id = int(movie_id)
                movies = mark_watched(movies, movie_id)
                print(f"Фильм с ID {movie_id} отмечен как просмотренный.")
            except ValueError:
                print("Ошибка: введите числовой ID фильма.")

        elif choice == "4":
            search_year = input("Введите год для поиска фильмов: ")
            try:
                search_year = int(search_year)
                found_movies = find_by_year(movies, search_year)
                if found_movies:
                    print(f"\nФильмы выпущенные в {search_year}:")
                    display_movies(found_movies)
                else:
                    print(f"Фильмов, выпущенных в {search_year}, не найдено.")
            except ValueError:
                print("Ошибка: неверный формат года. Используйте цифры.")

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("До свидания!")
            break

        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
