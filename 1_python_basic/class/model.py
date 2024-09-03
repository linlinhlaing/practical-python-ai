

class Author:
    def __init__(self, birth_date: str, author_id: str, author_name: str):
        self.birth_date = birth_date
        self.id = author_id
        self.name = author_name

    def __repr__(self):
        return f"Author(birth_date={self.birth_date!r}, id={self.id!r}, name={self.name!r})"
  


class Book:
    def __init__(self, publication_date: str, book_id: str, title: str, isbn: str, price: float, author: Author):
        self.publication_date = publication_date
        self.title = title
        self.id = book_id
        self.isbn = isbn
        self.price = price
        self.author = author

    def __repr__(self):
        return (f"Book(publication_date={self.publication_date!r}, id={self.id!r}, "
                f"title={self.title!r}, isbn={self.isbn!r}, price={self.price!r}, "
                f"author={self.author!r})")    

    def getDiscountedPrice(self, discount_rate: float):
        """Calculate discounted price based on a discount rate."""
        return self.price * (1 - discount_rate)
    

