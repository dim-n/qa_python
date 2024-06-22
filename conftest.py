import pytest

import data


@pytest.fixture
def make_a_list():  # Вернет фантастику
    temp = []
    for name, genre in data.name.items():
        if genre == 'Фантастика':
            temp.append(name)
    return temp


@pytest.fixture
def make_a_list_children():  # Вернет список для детей
    temp = []
    for name, genre in data.name.items():
        if genre != 'Ужасы' and genre != 'Детективы':
            temp.append(name)
    return temp


@pytest.fixture
def make_a_list_range():  # Вернет словарь для взрослых
    temp_dict = {}
    for name, genre in data.name.items():
        if genre == 'Ужасы' or genre == 'Детективы':
            temp_dict[name] = genre
    return temp_dict
