import data


def make_a_list_one_name_and_genre():  # Вернет только одну книгу и жанр
    one_name_genre = []
    for name, genre in data.name.items():
        if name == 'Фантастика':
            one_name_genre.append(genre[0])
            one_name_genre.append(name)
    return one_name_genre

def all_book_and_genres(): # Вернет все книги и их жанры в виде словаря
    result_dict = {}
    for name, genre in data.name.items():
        for i in genre:
            if i not in result_dict.keys():
                result_dict[i] = name
    return result_dict


def helpers_adult_books():  # Вернет книги и их жанры для взрослых
    result_dict = {}
    for name, genre in data.name.items():
        if name == 'Ужасы' or name == 'Детективы':
            for i in genre:
                result_dict[i] = name
    return result_dict


long_name = 'Гарри Поттер и философский камень фантастика'


def books_for_kids():  # Вернет список для детей
    result_dict = []
    for name, genre in data.name.items():
        if name != 'Ужасы' and name != 'Детективы':
            for i in genre:
                result_dict.append(i)
    return result_dict

