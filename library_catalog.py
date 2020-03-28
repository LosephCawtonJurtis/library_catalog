from abc import ABC, abstractmethod

"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""


class LibraryItem(ABC):
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
        # return f'{self.name}\n{self.isbn}\n{self.resource_type}\n{", ".join(self.tags)}'
        # I made an edit in your code here because I think that I just don't understand how you
        # want tags to work and if this is all it takes to get my understanding of tags to function
        # I'm hoping that will be understandable
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\n,{self.tags}'

    def to_short_string(self):
        """Return a short string representation of the item

        String contains only the name of the item and the type of the item
        I.E.
        Moby Dick - eBook
        All subclasses must provide a to_short_string method
        """
        return f'{self.name} - {self.isbn}'


class Book(LibraryItem):
    '''many functions are repeated with minor changes so they will only be described in this class
    Book extends library item'''

    def __init__(self, name, isbn, author, tags=None):
        """ initializes an instance of a subclass and defines it's base attributes and functions
        :param:
        name - name of the instance
        isbn - isbn of the instance
        tags - not utilized yet

        author - subclass specific parameter denoting the author of the book

        :returns:
        nothin
        """
        super().__init__(name, isbn, tags) # call to the super class for predefined parameters
        self.author = author
        self.resource_type = 'Book'

    def match(self, filter_text):
        """ match defines the terms you can use to search for the instance inside of the catalog
        :param:
        filter_text - the text given by the user to perform the search with
        :return:
        returns a boolean value based on whether the filter text matched any attribute values that the instance
        can be searched by
        """
        return super().match(filter_text) or self.author == filter_text

    def __str__(self):
        """converts the attribute values of a given class to a user readable format to convey information about the physical
        object being represented
        :return:
        returns a more readable list of attributes
        """
        return super().__str__() + '\n' + self.author

    def to_short_string(self): # performs the same action as above but returns an abbreviated list
        return self.name + '-' + self.resource_type + '-' + self.isbn

    @classmethod
    def create_book(cls):
        """ gathers all data from a user that is required to create a subclass instance
        :return:
        data to fill in attributes when instantiating an instance of a subclass
        """
        name = input('name of book: ')
        isbn = input('isbn of book: ')
        author = input('author of book: ')
        tags = CategoryTags.create_or_choose_tag()

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

    def to_short_string(self):
        return self.name + '-' + self.resource_type + '-' + self.isbn

    @classmethod
    def create_DVD(cls):
        name = input('name of DVD: ')
        isbn = input('isbn of DVD: ')
        runtime = input('runtime of DVD: ')
        rating = input('rating of DVD: ')
        tags = CategoryTags.create_or_choose_tag()

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

    def to_short_string(self):
        return self.name + '-' + self.resource_type + '-' + self.isbn

    @classmethod
    def create_software(cls):
        name = input('name of software: ')
        isbn = input('isbn of software: ')
        purpose = input('purpose of software: ')
        tags = CategoryTags.create_or_choose_tag()

        return cls(name, isbn, purpose, tags)


class CategoryTags:
    """"""
    _all_tags = []

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return super().__str__() + '\n' + self.name + '-' + self.description

    def to_short_string(self):
        return self.name + '-' + self.description

    @classmethod
    def all_category_tags(cls):
        for tag in cls._all_tags:
            print(tag.to_short_string())

    @classmethod
    def create_or_choose_tag(cls):
        user_input = input('would you like to create a new tag or use an existing one?(create/use): ')
        if user_input == 'create':
            name = input('input tag name: ')
            description = input('describe the tag: ')
            return_tag = cls(name, description)
            cls._all_tags.append(return_tag)
            return return_tag
        else:
            cls.all_category_tags()
            user_input = input('enter the name of the tag you would like to use: ')
            for tag in cls._all_tags:
                if user_input == tag.name:
                    print('yeet')
                    return_tag = cls(str(tag.name), str(tag.description))
                    return return_tag



class Catalog:
    """ primary structure for storing all libraryitem based objects as well as defines UI logic for interacting with
    the program"""

    def __init__(self, name):  # class initializer
        self.name = name
        self._private_list_ = []

    def search_library(self, search_term):
        """ iterates through all objects in the catalog's list to find any that have search_term matching data for a
        specific attribute as the search term

        :param:
        search_term - the term given by the user to match with attribute data in given objects
        :return:
        returns a list of all objects that had matching pieces of data
        """
        filtered_items = []
        for item in self._private_list_:
            if item.match(search_term):
                filtered_items.append(item)
        return filtered_items

    def remove_item(self, name):
        """ iterates through all items in the list to find any that match the name given before removing them from the
        catalog

        :param:
        name - the object name being searched for
        :return:
        returns nothing
        """
        for items in self._private_list_:
            if items.name == name:
                self._private_list_.remove(items)
        pass

    def add_item(self, new_item):
        """ adds an already created item to the catalog

        :param:
        new_item - the name of the item to be added
        :return:
        returns nothing
        """
        self._private_list_.append(new_item)

    def print_whole(self):
        """ iterates through the entire catalog and prints the abridged data for each item
        :return:
        returns nothing
        """
        for item in self._private_list_:
            print(item.to_short_string())


if __name__ == "__main__":  # test code that seems like it's worth keeping as a reference for part 2
    # library = Catalog('Champlain Library')
    # book1 = Book('Harry Potter','23423','JK Rowling')
    # library.add_item(book1)
    # book2 = Book.create_book()
    # library.add_item(book2)
    # software1 = software.create_software()
    # library.add_item(software1)
    # search_results = library.search_library('JK Rowling')
    # print(f'Search Results: ')
    # print(*search_results)
    # library.print_whole()
    CategoryTags.create_or_choose_tag()
    CategoryTags.all_category_tags()
