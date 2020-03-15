from library_catalog import LibraryItem, Book, Catalog, DVD, software

menu = """
    Library Catalog Menu

    1. Search Catalog
    2. Print the entire catalog
    3. Add item to catalog
    4. remove item from catalog

    Choose an option
           """
item_list = """
    Choose a type of item to create
    
    1. DVD
    2. Book 
    3. Software
        """

library = Catalog('Champlain Library')


def display_menu():
    x = int(input(menu))
    return x


def display_item_type():
    x = int(input(item_list))
    return x


while True:
    user_input = display_menu()

    if user_input == 1: # search
        search_results = library.search_library(input('input search term here: '))
        print(*search_results)
        print('yes')
    elif user_input == 2: # print whole
        library.print_whole()
    elif user_input == 3: # add item
        if display_item_type() == 1:
           item_to_add = DVD.create_DVD()
        elif display_item_type() == 2:
            item_to_add = Book.create_book()
        else:
            item_to_add = software.create_software()
        library.add_item(item_to_add)
    elif user_input == 4:
        library.remove_item(input('name of item: '))
user_input = display_menu()