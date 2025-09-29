import pytest
from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
    
    @pytest.mark.parametrize('name', ['', 'Очень длинное название книги, которое превышает лимит в 40 символов'])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0
    
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1
    
    def test_set_book_genre_for_existing_book_with_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        assert collector.get_book_genre('Ужасная книга') == 'Ужасы'
    
    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None
    
    def test_set_book_genre_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга') == ''
    
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        collector.add_new_book('Другая фантастика')
        collector.set_book_genre('Другая фантастика', 'Фантастика')
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 2
        assert 'Фантастическая книга' in fantasy_books
    
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Мультфильм')
        collector.set_book_genre('Мультфильм', 'Мультфильмы')
        collector.add_new_book('Ужас')
        collector.set_book_genre('Ужас', 'Ужасы')
        
        children_books = collector.get_books_for_children()
        assert 'Мультфильм' in children_books
        assert 'Ужас' not in children_books
    
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()
    
    def test_add_nonexistent_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0
    
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()
    
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Детектив')
        collector.set_book_genre('Детектив', 'Детективы')
        assert collector.get_book_genre('Детектив') == 'Детективы'