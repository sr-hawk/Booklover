import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    
    def test_1_add_book(self):
        test_lover = BookLover("Loves Books", "love@books.com", "all books")
        test_lover.add_book("Jane Eyre", 4)
        assert True if (test_lover.book_list == "Jane Eyre").any().any() else False
        
    def test_2_add_book(self):
        test_lover = BookLover("Loves Books", "love@books.com", "all books")
        test_lover.add_book("Fight Club", 3)
        test_lover.add_book("Fight Club", 3)
        test_lover.book_list.value_counts('book_name')['Fight Club']
        assert True if test_lover.book_list.value_counts('book_name')['Fight Club'] < 2 else False

    def test_3_has_read(self):
        test_lover = BookLover("Loves Books", "love@books.com", "all books")
        test_lover.add_book("Fight Club", 3)
        assert test_lover.has_read("Fight Club")
        
    def test_4_has_read(self):
        test_lover = BookLover("Loves Books", "love@books.com", "all books")
        assert not (test_lover.has_read("Enders Game"))
        
    def test_5_num_books_read(self):
        test_lover = BookLover("Loves Books", "love@books.com", "all books")
        test_lover.add_book("Book 1", 4)
        test_lover.add_book("Book 2", 3)
        test_lover.add_book("Book 3", 3)
        test_lover.add_book("Book 4", 3)
        assert test_lover.num_books_read() == 4
        
    def test_6_fav_books(self):
        test_lover = BookLover("Loves Books", "love@books.com", "all books")
        test_lover.add_book("Book 7", 4)
        test_lover.add_book("Book 8", 5)
        fav_book_list = test_lover.fav_books()
        assert False if (test_lover.fav_books()['book_rating'] < 4).any() else True

if __name__ == '__main__':
    
    unittest.main(verbosity=3)