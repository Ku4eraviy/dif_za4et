import os
import tempfile
import json
import pytest
from movies_manager.logic import load_movies, add_movie, mark_watched, find_by_year


@pytest.fixture
def empty_json_file(tmpdir):
    filename = tmpdir.join('empty.json')
    with open(filename, 'w') as fp:
        json.dump([], fp)
    yield str(filename)
    os.remove(str(filename))


@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'title': 'Matrix', 'year': 1999, 'watched': False},
        {'id': 2, 'title': 'Inception', 'year': 2010, 'watched': True},
        {'id': 3, 'title': 'Interstellar', 'year': 2014, 'watched': False}
    ]


def test_load_movies_without_file():
    nonexistent_file = 'non_existent.json'
    assert load_movies(nonexistent_file) == [], \
        f"При отсутствии файла ожидался пустой список, но получено {load_movies(nonexistent_file)}"


def test_load_movies_with_empty_file(empty_json_file):
    loaded_movies = load_movies(empty_json_file)
    assert loaded_movies == [], \
        f"Из пустого файла ожидался пустой список, но получено {loaded_movies}"


def test_add_movie(sample_data):
    original_length = len(sample_data)
    added_movie = {'id': 4, 'title': 'Avatar', 'year': 2009, 'watched': False}
    updated_movies = add_movie(sample_data[:], added_movie['title'], added_movie['year'])
    assert len(updated_movies) == original_length + 1, \
        f"Количество фильмов не увеличилось после добавления."
    last_movie = updated_movies[-1]
    assert last_movie['title'] == added_movie['title'], \
        f"Название последнего фильма отличается от ожидаемого."
    assert last_movie['year'] == added_movie['year'], \
        f"Год последнего фильма отличается от ожидаемого."
    assert last_movie['watched'] is False, \
        f"Статус просмотра должен быть False для вновь добавленного фильма."


def test_mark_watched(sample_data):
    target_id = 1
    expected_title = 'Matrix'
    updated_movies = mark_watched(sample_data[:], target_id)
    for movie in updated_movies:
        if movie['id'] == target_id:
            assert movie['watched'] is True, \
                f"Фильм с ID={target_id} ({expected_title}) не стал просмотренным."
            break
    else:
        raise AssertionError(f"Фильм с ID={target_id} не найден в списке.")


def test_find_by_year(sample_data):
    target_year = 2010
    results = find_by_year(sample_data, target_year)
    assert len(results) == 1, \
        f"Количество фильмов с годом {target_year} должно быть ровно одно."
    first_result = results[0]
    assert first_result['title'] == 'Inception', \
        f"Первый фильм с искомым годом {target_year} должен быть Inception."
    assert first_result['year'] == target_year, \
        f"Год первого результата не соответствует ожидаемому значению {target_year}."