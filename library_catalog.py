"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""


class LibraryItem:
    """Base class for all items stored in a library catalog

    Provides a simple LibraryItem with only a few attributes

    """

    def __init__(self, name, isbn, tags=None):
        """Initialize a LibraryItem

        :param name: (string) Name of item
        :param isbn: (string) ISBN number for the item
        :param tags: (list) List of CategoryTags

        self.name = name
        self.isbn = isbn
        self.tags = tags
        self.resource_type = 'Generic'  # This is the type of item being stored
        """
        self.name = name
        self.isbn = isbn
        if tags:
            self.tags = tags
        else:
            self.tags = list()
            self.resource_type = 'Generic'

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match or
        partial match.

        match needs to be redefined for any subclasses.  Please see the
        note/notebook case study from Chapter 2 as an example of how match
        is designed to work.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() in (str(tag).lower() for tag in self.tags)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        """
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item

        String contains only the name of the item and the type of the item
        I.E.
        Moby Dick - eBook
        All subclasses must provide a to_short_string method
        """
        return f'{self.name} - {self.isbn}'


class Book(LibraryItem):

    def __init__(self, name, isbn, author, tags=None):
        super().__init__(name, isbn, tags)
        self.author = author
        self.resource_type = 'Book'

    def match(self, filter_text):
        return super().match(filter_text) or self.author == filter_text

    def __str__(self):
        return super().__str__() + '\n' + self.author

    @classmethod
    def create_book(cls):
        name = input('name of book: ')
        isbn = input('isbn of book: ')
        author = input('author of book: ')
        tags = None

        return cls(name, isbn, author, tags)


class DVD(LibraryItem):

    def __init__(self, name, isbn, runtime, rating, tags=None):
        super().__init__(name, isbn, tags)
        self.rating = rating
        self.resource_type = 'DVD'
        self.runtime = runtime

    def match(self, filter_text):
        return super().match(filter_text) or filter_text == self.rating

    def __str__(self):
        return super().__str__() + '\n' + self.runtime + '\n' + self.rating

    @classmethod
    def create_DVD(cls):
        name = input('name of DVD: ')
        isbn = input('isbn of DVD: ')
        runtime = input('runtime of DVD: ')
        rating = input('rating of DVD: ')
        tags = None

        return cls(name, isbn, runtime, rating, tags)


class software(LibraryItem):

    def __init__(self, name, isbn, purpose, tags=None):
        super().__init__(name, isbn, tags)
        self.purpose = purpose
        self.resource_type = 'Software'

    def match(self, filter_text):
        match = super().match(filter_text) or filter_text == self.purpose
        return match

    def __str__(self):
        return super().__str__() + '\n' + self.purpose

    @classmethod
    def create_software(cls):
        name = input('name of software: ')
        isbn = input('isbn of software: ')
        purpose = input('purpose of software: ')
        tags = None

        return cls(name, isbn, purpose, tags)


class Catalog:

    def __init__(self, name):
        self.name = name
        self._private_list_ = []

    def search_library(self, search_term):
        filtered_items = []
        for item in self._private_list_:
            if item.match(search_term):
                filtered_items.append(item)
        return filtered_items

    def remove_item(self, name):
        for items in self._private_list_:
            if items.name == name:
                self._private_list_.remove(items)
        pass

    def add_item(self, new_item):
        self._private_list_.append(new_item)

    def print_whole(self):
        for item in self._private_list_:
            print(item)


if __name__ == "__main__":
    library = Catalog('Champlain Library')
    book1 = Book('Harry Potter','23423','JK Rowlings')
    library.add_item(book1)
    book2 = Book.create_book()
    library.add_item(book2)
    software1 = software.create_software()
    library.add_item(software1)
    search_results = library.search_library('JK Rowlings')
    print(f'Search Results: ')
    print(*search_results)
    library.print_whole()
