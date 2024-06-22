import pytest
import data
from main import BooksCollector


class TestBooksCollector:

    # добавляем новую книгу
    def test_add_new_book(self):
        book = BooksCollector()
        book.add_new_book('Властелин колец')
        assert 'Властелин колец' in book.books_genre

    # добавляем новую книгу если название больше 40 символов
    def test_add_new_book_namesign_mt_40_faild(self):
        book = BooksCollector()
        assert book.add_new_book('Фродо Беггинс Властелин колец и философский камень') is None

    # устанавливаем книге жанр
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_set_book_genre(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.books_genre[name] == genre

    # устанавливаем книге жанр
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фентези')])
    def test_set_book_genre_not_found_faild(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        assert book.set_book_genre(name, genre) is None

    # получаем жанр книги по её имени
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_get_book_genre(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre(name) == genre

    # получаем жанр книги по её имени
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_get_book_genre_not_found_name_faild(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre('Король колец') != genre

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self, make_a_list):
        book = BooksCollector()
        book.books_genre = data.name
        assert book.get_books_with_specific_genre('Фантастика') == make_a_list  # фикстура вернет фантастику из дата

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_not_found_faild(self, make_a_list):
        book = BooksCollector()
        book.books_genre = data.name
        assert book.get_books_with_specific_genre('Роман') == []  # вернет пустой список

    # получаем словарь books_genre
    def test_get_books_genre(self):
        book = BooksCollector()
        book.books_genre = data.name
        assert book.books_genre == data.name

    # получаем словарь books_genre
    def test_get_books_genre_faild(self):
        book = BooksCollector()
        assert book.books_genre == {}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children(self, make_a_list_children):
        book = BooksCollector()
        book.books_genre = data.name
        assert book.get_books_for_children() == make_a_list_children  # фикстура вернет список для детей из дата

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_not_found_child_faild(self, make_a_list_range):
        book = BooksCollector()
        book.books_genre = make_a_list_range
        assert book.get_books_for_children() == []  # фикстура вернет список только для взрослых

    # добавляем книгу в Избранное
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_add_book_in_favorites(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.add_book_in_favorites(name)
        assert book.favorites == [name]

    # добавляем книгу в Избранное
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_add_book_in_favorites_if_not_in_book_genere_faild(self, name, genre):
        book = BooksCollector()
        book.add_book_in_favorites(name)
        assert book.favorites != [name]

    # удаляем книгу из Избранного
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_delete_book_from_favorites(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.add_book_in_favorites(name)
        book.delete_book_from_favorites(name)
        assert book.favorites == []

    # удаляем книгу из Избранного
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_delete_book_from_favorites_not_try_book_faild(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.add_book_in_favorites(name)
        assert book.delete_book_from_favorites('Король колец') is None

    # получаем список Избранных книг
    @pytest.mark.parametrize('name,genre', [('Властелин колец', 'Фантастика')])
    def test_get_list_of_favorites_books(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.add_book_in_favorites(name)
        assert book.favorites == [name]

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_add_one_to_fav(self, make_a_list_range):
        book = BooksCollector()
        book.books_genre = make_a_list_range
        book.add_book_in_favorites('Гремлины')
        assert book.favorites == ['Гремлины']
