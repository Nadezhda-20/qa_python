import pytest
from main import BooksCollector

class TestBooksCollector:    
    
    def test_add_new_book_add_two_books(self,collector):    
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')        
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['', 'Очень длинное название книги, которое превышает лимит в 40 символов'])
    def test_add_new_book_invalid_name_length(self,collector, name):        
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_duplicate_not_added(self,collector):        
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_for_existing_book_with_valid_genre(self,collector):
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        assert collector.books_genre['Ужасная книга'] == 'Ужасы'

    def test_set_book_genre_for_nonexistent_book(self,collector):
        
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.books_genre

    def test_set_book_genre_with_invalid_genre(self,collector):
        
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.books_genre['Книга'] == ''

    def test_get_books_with_specific_genre(self,collector):
        
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        collector.add_new_book('Детективная книга')
        collector.set_book_genre('Детективная книга', 'Детективы')
        collector.add_new_book('Другая фантастика')
        collector.set_book_genre('Другая фантастика', 'Фантастика')
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert set(fantasy_books) == {'Фантастическая книга', 'Другая фантастика'}
        

    def test_get_books_for_children(self,collector):
        
        collector.add_new_book('Мультфильм')
        collector.set_book_genre('Мультфильм', 'Мультфильмы')
        collector.add_new_book('Ужас')
        collector.set_book_genre('Ужас', 'Ужасы')
        collector.add_new_book('Комедия')
        collector.set_book_genre('Комедия', 'Комедии')
        
        children_books = collector.get_books_for_children()
        assert set(children_books) == {'Мультфильм', 'Комедия'}
        

    def test_add_book_in_favorites(self,collector):
        
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.favorites

    def test_add_nonexistent_book_in_favorites(self, collector):
        
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites(self, collector):
        
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.favorites

    def test_get_book_genre_positive(self, collector):
        
        collector.add_new_book('Детектив')
        collector.books_genre['Детектив'] = 'Детективы'
        assert collector.get_book_genre('Детектив') == 'Детективы'

    def test_get_book_genre_for_nonexistent_book(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_genre(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        books_genre = collector.get_books_genre()
        assert books_genre is collector.books_genre
        assert len(books_genre) == 2

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_book_in_favorites('Книга1')
        favorites = collector.get_list_of_favorites_books()
        assert favorites is collector.favorites
        assert len(favorites) == 1
        assert 'Книга1' in favorites

