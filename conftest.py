import pytest
import helpers
from main import BooksCollector


@pytest.fixture()
def book():
    """Фикстура нужна чтобы создать экземпляр класса"""
    book = BooksCollector()
    return book


@pytest.fixture()
def all_book_and_genres(book):
    """Фикстура нужна чтобы добавить в список книг обьекта
    с названиями и жанрами, all_book_and_genres содержит словарь который получил из хелпера
    вызываются два метода для этого add_new_book(key) добавит название книги,
    а set_book_genre(key, value) добавит ему жанр"""
    all_book_and_genres = helpers.all_book_and_genres()
    for key, value in all_book_and_genres.items():
        book.add_new_book(key)
        book.set_book_genre(key, value)
    return book


@pytest.fixture()
def adult_books(book):
    """Фикстура создаст словарь внутри обьекта с книгами и жанрами,
     adult_books содержит словарь с ограничением по возрасту получивший из хелпера"""
    adult_books = helpers.helpers_adult_books()
    for key, value in adult_books.items():
        book.add_new_book(key)
        book.set_book_genre(key, value)
    return book


@pytest.fixture()
def favorite_books(book):
    """Фикстура получает словарь всех книг и жанра из хелпера и
    добавляет названия в избранные"""
    favorite_books = helpers.all_book_and_genres()
    for key in favorite_books.keys():
        book.add_book_in_favorites(key)
        return book
