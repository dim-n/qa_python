import data
import helpers


class TestBooksCollector:

    # добавляем новую книгу
    def test_add_new_book(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр]
        название добавляется в метод add_new_book, название находиться по индексу 0 а жанр 1
        проверяется, что создался словарь с названием вместо ключа и пустым значением"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        assert book.books_genre == {one_book_and_genre[0]: ''}

    # добавляем новую книгу если название больше 40 символов
    def test_add_new_book_namesign_mt_40_faild(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        в метод передается из data название длинна которой больше 40
        ожидается, что функция не создаст словарь"""
        assert book.add_new_book(helpers.long_name) is None

    # устанавливаем книге жанр
    def test_set_book_genre(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        add_new_book() добавляем название книги
        set_book_genre() передаем название и жанр, чтобы метод нашел, что название есть в словаре,
        тогда можно указать ему жанр и проверяется жанр добавленной книги совпадает с тем что в списке"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.set_book_genre(one_book_and_genre[0], one_book_and_genre[1])
        assert book.books_genre[one_book_and_genre[0]] == one_book_and_genre[1]

    # устанавливаем книге жанр
    def test_set_book_genre_not_found_faild(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        add_new_book() добавляем название книги
        методу передаем существующее название книги и несуществующий жанр
        метод должен проверить, есть ли такой жанр в списке, если нет жанр не добавиться к названию"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        assert book.set_book_genre(one_book_and_genre[0], 'Фентези') is None

    # получаем жанр книги по её имени
    def test_get_book_genre(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        передаем в метод название и получаем жанр и сравниваем с жанром в списке"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        assert book.get_book_genre(one_book_and_genre[0]) == one_book_and_genre[1]

    # получаем жанр книги по её имени
    def test_get_book_genre_not_found_name_faild(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        передаем в метод не существующее название метод ничего не вернет значит он не равен жанру в списке"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        assert book.get_book_genre('Король колец') != one_book_and_genre[1]

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        Передаем в метод жанр фантастика и метод вернет названия книг,
        и сравниваем с значением словаря data.name где в значениях лежат названия книг"""
        assert book.get_books_with_specific_genre('Фантастика') == data.name['Фантастика']

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_not_found_faild(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        в метод передаем несуществующий жанр и ожидается пустой список"""
        assert book.get_books_with_specific_genre('Роман') == []  # вернет пустой список

    # получаем словарь books_genre
    def test_get_books_genre(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        all_book_and_genres содержит словарь из названий и жанров всех книг
        аргумент обьекта сравниваем с all_book_and_genres"""
        all_book_and_genres = helpers.all_book_and_genres()
        assert book.books_genre == all_book_and_genres

    # получаем словарь books_genre
    def test_get_books_genre_none(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        т.к. обьект создается а не заполняется словарь, сравниваем с пустым словарем"""
        assert book.books_genre == {}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        books_for_kids содержит список названий книг без жанров ужасы и детективы
        при вызове метода он создает список названий книг для детей ее сравниваем со списоком без ужасы и детективы"""
        books_for_kids = helpers.books_for_kids()
        assert book.get_books_for_children() == books_for_kids

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_not_found_child_faild(self, book, adult_books):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        adult_books фикстура добавить в словарь обьекта названия книг жанра ужасы и детективы
        при вызове метода не найдет подходящие жанры и вернет пустой список"""
        assert book.get_books_for_children() == []  # фикстура вернет список только для взрослых

    # добавляем книгу в Избранное
    def test_add_book_in_favorites(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        add_new_book() создали словарь из одной книги без жанра
        add_book_in_favorites() проверит есть ли название в словаре, если есть добавить в избранные
        сравниваем словарь избранных книг равен ли списку из переданного названия"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.add_book_in_favorites(one_book_and_genre[0])
        assert book.favorites == [one_book_and_genre[0]]

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_if_not_in_book_genere_faild(self, book, all_book_and_genres):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        методу передаем название, он проверяет, что названия нет в словаре и не добавит в избранные"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        assert book.add_book_in_favorites(one_book_and_genre[0]) is None

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        add_new_book добавили в словарь одно название
        add_book_in_favorites добавили в избранное одно название
        delete_book_from_favorites удалили из избранного одно название
        favorites сраниваем с пустым списком"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.add_book_in_favorites(one_book_and_genre[0])
        book.delete_book_from_favorites(one_book_and_genre[0])
        assert book.favorites == []

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_not_try_book_faild(self, book, all_book_and_genres, favorite_books):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        all_book_and_genres фикстура чтобы создать в обьекте словарь со всеми названиями и жанрами
        favorite_books добавляем названия в избранные
        передаем методу несущестующее название, метод ничего не удалит"""
        assert book.delete_book_from_favorites('Король колец') is None

    # получаем список Избранных книг
    def test_get_list_of_favorites_books(self, book):
        """Вызывается book фикстура, чтобы создать экземпляр класса,
        one_book_and_genre содержит список в виде [название: жанр], название находиться по индексу 0 а жанр 1
        add_new_book добавили в словарь одно название
        add_book_in_favorites добавили в избранное одно название
        добавили одну книгу в избранные и сравниваем с одной книгой"""
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.add_book_in_favorites(one_book_and_genre[0])
        assert book.favorites == [one_book_and_genre[0]]
