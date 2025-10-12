from typing import Dict,List,Set

class Transaction:

         def __init__(self,lender:str,borrower: str, book: str, days: int):
               self.lender = lender
               self.borrower = borrower
               self.book = book
               self.days = days

         def get_borrower(self):
             return self.borrower

         def get_book(self):
             return self.book

         def get_days(self):
             return self.days
         def get_lender(self):
             return self.lender


class FineDTO:
    def __init__(self,fine: int, book_history: Set[str]):
        self.fine = fine
        self.book_history = book_history


class LibraryManager:



     def __init__(self, transaction_list: List[Transaction]):
         self.transaction_list = transaction_list
         self.MAX_ALLOWED_DAYS = 10
         self.borrower_fine_record : Dict[str, FineDTO] = {}
         self.book_record : Dict[str, int] = {}

     def calculate_fine(self):
         for record in self.transaction_list:
             borrower = record.get_borrower()
             book = record.get_book()
             days = record.get_days()

             cal_book_fine = self.book_record.get(book,0)
             total_days_fine = cal_book_fine + days
             self.book_record[book] = total_days_fine

             if total_days_fine <= self.MAX_ALLOWED_DAYS:
                 continue

             if cal_book_fine <= 10:
                 borrower_fine = abs(10-total_days_fine)
             else :
                 borrower_fine = days

             self.borrower_fine_record.setdefault(borrower,FineDTO(0,set()))
             borrower_record = self.borrower_fine_record.get(borrower)
             fine = borrower_record.fine + borrower_fine
             borrower_books = borrower_record.book_history
             borrower_books.add(book)

             self.borrower_fine_record[borrower] = FineDTO(fine,borrower_books)
         self.print_record()



     def print_record(self):

         for borrower, values in self.borrower_fine_record.items():
               if values.fine == 0: continue
               value_list = list(values.book_history)
               books_taken = ",".join(value_list)
               print(f"{borrower}:{values.fine}:{books_taken}")



if __name__ == "__main__":
    transaction_lists = [Transaction("LIB", "Ace", "B1", 5),
        Transaction("ACE", "Bob", "B1", 7),
        Transaction("Bob", "LIB", "B1", 0),
        Transaction("Bob", "TAS", "B1", 6),
        Transaction("Tob", "BIB", "B2", 8),
        Transaction("Tob", "BIB", "B2", 5),
        Transaction("Tob", "BIB", "B2", 6),
        Transaction("Tob", "BIB", "B3", 26)]

    library_manager = LibraryManager(transaction_lists)
    library_manager.calculate_fine()
