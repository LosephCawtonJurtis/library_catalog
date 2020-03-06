from library_catalog import LibraryItem, Book, Catalog

menu = """
    Library Catalog Menu

    1. Search Catalog
    2. Print the entire catalog
    3. Add item to catalog
    4. remove item from catalog

    Choose an option
           """


def display_menu(self):
    x = int(input(self.menu))
    return x

while True:
    user_input = display_menu()

    if user_input == 1:
        Catalog.search_library(input('input search term here: '))
    elif user_input == 2:
        Catalog.print_whole()
    elif user_input == 3:
        check = input('do you want to create an item? yes/no: ')
        if check == 'yes':
            creation_type = input('create a book, dvd, or software')

    elif user_input == 4:


user_input = display_menu()