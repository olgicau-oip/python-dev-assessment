class Book:
    """A class to represent a book."""

    def __init__(self, title, author, isbn, publication_year):
        """
        Initialize a Book instance.

        Args:
            title: The title of the book
            author: The author of the book
            isbn: The ISBN of the book
            publication_year: The year the book was published
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        """
        Calculate and return the age of the book.

        Returns:
            The age of the book in years (current year 2026 - publication_year)
        """
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        """
        Return a summary of the book.

        Returns:
            A formatted string with title, author, and publication year
        """
        return (
            f"Title: {self.title}, Author: {self.author}, "
            f"Published: {self.publication_year}"
        )


# Example usage of the Book class
if __name__ == "__main__":
    # Create instances of Book
    book1 = Book(
        "The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925
    )
    book2 = Book(
        "To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960
    )
    book3 = Book(
        "1984", "George Orwell", "978-0451524935", 1949
    )

    # Test get_summary() method
    print("Book Summaries:")
    print(book1.get_summary())
    print(book2.get_summary())
    print(book3.get_summary())
    print()

    # Test get_age() method
    print("Book Ages:")
    print(f"{book1.title} is {book1.get_age()} years old")
    print(f"{book2.title} is {book2.get_age()} years old")
    print(f"{book3.title} is {book3.get_age()} years old")
