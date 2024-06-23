# qa_python
Приложение BooksCollector

    # добавляем новую книгу
    def test_add_new_book(self, book):

    # добавляем новую книгу если название больше 40 символов
    def test_add_new_book_namesign_mt_40_faild(self, book):        

    # устанавливаем книге жанр
    def test_set_book_genre(self, book):        

    # устанавливаем книге жанр
    def test_set_book_genre_not_found_faild(self, book):
        
    # получаем жанр книги по её имени
    def test_get_book_genre(self, book, all_book_and_genres):
        
    # получаем жанр книги по её имени
    def test_get_book_genre_not_found_name_faild(self, book, all_book_and_genres):

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self, book, all_book_and_genres):
        
    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_not_found_faild(self, book, all_book_and_genres):       

    # получаем словарь books_genre
    def test_get_books_genre(self, book, all_book_and_genres):       

    # получаем словарь books_genre
    def test_get_books_genre_none(self, book):        

    # возвращаем книги, подходящие детям
    def test_get_books_for_children(self, book, all_book_and_genres):

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_not_found_child_faild(self, book, adult_books):
       
    # добавляем книгу в Избранное
    def test_add_book_in_favorites(self, book):
        
    # добавляем книгу в Избранное
    def test_add_book_in_favorites_if_not_in_book_genere_faild(self, book, all_book_and_genres):
        
    # удаляем книгу из Избранного
    def test_delete_book_from_favorites(self, book):

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_not_try_book_faild(self, book):

    # получаем список Избранных книг
    def test_get_list_of_favorites_books(self, book):

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_add_one_to_fav(self, book):
        
