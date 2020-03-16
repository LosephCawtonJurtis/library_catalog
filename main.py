from library_catalog import LibraryItem, Book, Catalog, DVD, software
# imports


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
    """ displays the pre defined menu
    :return:
    returns the users decision
    """
    x = int(input(menu))
    return x


def display_item_type():
    """ displays a predefined list of options when creating a new instance to be added
    :return:
    returns the user's choice
    """
    x = int(input(item_list))
    return x


while True:
    """ primary loop, the entire program takes place here as this is where the user's input is taken
    """
    user_input = display_menu()  # displays the predefined menu

    if user_input == 1: # searches based on user input
        search_results = library.search_library(input('input search term here: '))
        print(*search_results)
    elif user_input == 2: # prints whole catalog
        library.print_whole()
    elif user_input == 3: # creates and adds items based on user input
        if display_item_type() == 1:
           item_to_add = DVD.create_DVD()
        elif display_item_type() == 2:
            item_to_add = Book.create_book()
        else:
            item_to_add = software.create_software()
        library.add_item(item_to_add)
    elif user_input == 4:  # removes an item based on user input
        library.remove_item(input('name of item: '))
user_input = display_menu()