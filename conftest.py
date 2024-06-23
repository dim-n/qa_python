import pytest
import helpers
from main import BooksCollector


@pytest.fixture()
def book():
    book = BooksCollector()
    return book


@pytest.fixture()
def all_book_and_genres(book):
    all_book_and_genres = helpers.all_book_and_genres()
    for key, value in all_book_and_genres.items():
        book.add_new_book(key)
        book.set_book_genre(key, value)
    return book


@pytest.fixture()
def adult_books(book):
    adult_books = helpers.helpers_adult_books()
    for key, value in adult_books.items():
        book.add_new_book(key)
        book.set_book_genre(key, value)
    return book


@pytest.fixture()
def favorite_books(book, all_book_and_genres):
    for key, name in helpers.all_book_and_genres():
        book.add_book_in_favorites(key)
        return book
