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

    def __str__(self, object_target):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        """
        # return f'{self.name}\n{self.isbn}\n{self.resource_type}\n{", ".join(self.tags)}'
        if object_target.author:
            text = f'{object_target.name} has and isbn of {object_target.isbn} and is authored by {object_target.author}'
        elif object_target.rating:
            text = f'{object_target.name} has and isbn of {object_target.isbn} and is rated {object_target.rating} with a runtime of {object_target.runtime}'
        elif object_target.purpose:
            text = f'{object_target.name} has and isbn of {object_target.isbn} and has a purpose of {object_target.purpose}'
        return text

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

    def match(self, filter_text):
        return super().match() or self.author == filter_text


class DVD(LibraryItem):

    def __init__(self, name, isbn, runtime, rating, tags=None):
        super().__init__(self, name, isbn, tags)
        self.rating = rating
        self.runtime = runtime

    def match(self, filter_text):
        return super().match(self, filter_text) or filter_text == self.rating



class Software(LibraryItem):

    def __init__(self, name, isbn, purpose, tags=None):
        super().__init__(self, name, isbn, tags)
        self.purpose = purpose

    def match(self, filter_text):
        match = super().match(filter_text) or filter_text == self.purpose
        return match


class Catalog:
    _private_list_ = []
    menu = """
    Library Catalog Menu
    
    1. Search Catalog
    2. Print the entire catalog
    3. Add item to catalog
    4. remove item from catalog
    
    Choose an option
           """


    def __init__(self, name):
        self.name = name
        self._private_list_ = []

    @staticmethod
    def str(object_target):
        if object_target.i_type == 'book':
            text = f'{object_target.name} has and isbn of {object_target.isbn} and is authored by {object_target.author}'
        elif object_target.i_type == 'dvd':
            text = f'{object_target.name} has and isbn of {object_target.isbn} and is rated {object_target.rating} with a runtime of {object_target.runtime}'
        elif object_target.i_type == 'software':
            text = f'{object_target.name} has and isbn of {object_target.isbn} and has a purpose of {object_target.purpose}'
        return 'test'


    def display_menu(self):
        x = int(input(self.menu))
        return x

    def search_library(self, name):
        filtered_items = []
        start_length_items = len(filtered_items)
        for items in self._private_list_:
            if items.name == name:
                text = items.__str__(items)
                filtered_items.append(text)
        if len(filtered_items) > start_length_items:
            return filtered_items
        else:
            return "item not in Catalog"

    def remove_item(self, name,):
        for items in self._private_list_:
            if items.name == name:
                self._private_list_.remove(items)
        pass

    def add_item(self, name, isbn, i_type):
        if i_type == 'book':
            addition = Book(name, isbn, str(input("input author's name here ")))
        elif i_type == 'dvd':
            addition = DVD(name, isbn, str(input('input runtime here ')), str(input('input rating here ')))
        elif i_type == 'software':
            addition = Software(name, isbn, str(input('input purpose here, ie photo editing ')))
        self._private_list_.append(addition)

    def print_whole(self):
        for items in self._private_list_:
            print(str(Catalog.__str__(items)))
            print(items.__str__(items))



