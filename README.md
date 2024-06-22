# qa_python
Приложение BooksCollector

    # добавляем новую книгу Позитивная проверка
    def test_add_new_book():

    # добавляем новую книгу если название больше 40 символов Негативная проверка
    def test_add_new_book_namesign_mt_40_faild():
        
    # устанавливаем книге жанр Позитивная проверка
    def test_set_book_genre():

    # устанавливаем книге жанр Негативная проверка
    def test_set_book_genre_not_found_faild():

    # получаем жанр книги по её имени Позитивная проверка
    def test_get_book_genre():
    
    # получаем жанр книги по её имени Негативная проверка
    def test_get_book_genre_not_found_name_faild():

    # выводим список книг с определённым жанром Позитивная проверка
    def test_get_books_with_specific_genre():

    # выводим список книг с определённым жанром Негативная проверка
    def test_get_books_with_specific_genre_not_found_faild():

    # получаем словарь books_genre Позитивная проверка
    def test_get_books_genre():

    # получаем словарь books_genre Негативная проверка
    def test_get_books_genre_faild():

    # возвращаем книги, подходящие детям Позитивная проверка
    def test_get_books_for_children():

    # возвращаем книги, подходящие детям Негативная проверка
    def test_get_books_for_children_not_found_child_faild():

    # добавляем книгу в Избранное Позитивная проверка
    def test_add_book_in_favorites():

    # добавляем книгу в Избранное Негативная проверка
    def test_add_book_in_favorites_if_not_in_book_genere_faild():

    # удаляем книгу из Избранного Позитивная проверка
    def test_delete_book_from_favorites():

    # удаляем книгу из Избранного Негативная проверка
    def test_delete_book_from_favorites_not_try_book_faild():

    # получаем список Избранных книг Позитивная проверка
    def test_get_list_of_favorites_books():
    
    # получаем список Избранных книг Позитивная проверка
    def test_get_list_of_favorites_books_add_one_to_fav():
