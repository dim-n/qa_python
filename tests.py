import pytest
import data
import helpers
from main import BooksCollector
from helpers import make_a_list_one_name_and_genre


class TestBooksCollector:

    # добавляем новую книгу
    def test_add_new_book(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        assert book.books_genre == {one_book_and_genre[0]: ''}

    # добавляем новую книгу если название больше 40 символов
    def test_add_new_book_namesign_mt_40_faild(self, book):
        assert book.add_new_book(helpers.long_name) is None

    # устанавливаем книге жанр
    def test_set_book_genre(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.set_book_genre(one_book_and_genre[0], one_book_and_genre[1])
        assert book.books_genre[one_book_and_genre[0]] == one_book_and_genre[1]

    # устанавливаем книге жанр
    def test_set_book_genre_not_found_faild(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        assert book.set_book_genre(one_book_and_genre[0], 'Фентези') is None

    # получаем жанр книги по её имени
    def test_get_book_genre(self, book, all_book_and_genres):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        assert book.get_book_genre(one_book_and_genre[0]) == one_book_and_genre[1]

    # получаем жанр книги по её имени
    def test_get_book_genre_not_found_name_faild(self, book, all_book_and_genres):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        assert book.get_book_genre('Король колец') != one_book_and_genre[1]

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self, book, all_book_and_genres):
        assert book.get_books_with_specific_genre('Фантастика') == data.name['Фантастика']

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_not_found_faild(self, book, all_book_and_genres):
        assert book.get_books_with_specific_genre('Роман') == []  # вернет пустой список

    # получаем словарь books_genre
    def test_get_books_genre(self, book, all_book_and_genres):
        all_book_and_genres = helpers.all_book_and_genres()
        assert book.books_genre == all_book_and_genres

    # получаем словарь books_genre
    def test_get_books_genre_none(self, book):
        assert book.books_genre == {}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children(self, book, all_book_and_genres):
        books_for_kids = helpers.books_for_kids()
        assert book.get_books_for_children() == books_for_kids

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_not_found_child_faild(self, book, adult_books):
        assert book.get_books_for_children() == []  # фикстура вернет список только для взрослых

    # добавляем книгу в Избранное
    def test_add_book_in_favorites(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.add_book_in_favorites(one_book_and_genre[0])
        assert book.favorites == [one_book_and_genre[0]]

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_if_not_in_book_genere_faild(self, book, all_book_and_genres):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        assert book.add_book_in_favorites(one_book_and_genre[0]) is None

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_book_in_favorites(one_book_and_genre[0])
        book.delete_book_from_favorites(one_book_and_genre[0])
        assert book.favorites == []

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_not_try_book_faild(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.add_book_in_favorites(one_book_and_genre[0])
        assert book.delete_book_from_favorites('Король колец') is None

    # получаем список Избранных книг
    def test_get_list_of_favorites_books(self, book):
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.add_new_book(one_book_and_genre[0])
        book.add_book_in_favorites(one_book_and_genre[0])
        assert book.favorites == [one_book_and_genre[0]]

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_add_one_to_fav(self, book):
        all_book = helpers.all_book_and_genres()
        one_book_and_genre = helpers.make_a_list_one_name_and_genre()
        book.books_genre = all_book
        book.add_book_in_favorites(one_book_and_genre[0])
        assert book.favorites == [one_book_and_genre[0]]
