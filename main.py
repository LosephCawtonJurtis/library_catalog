from library_catalog import LibraryItem, Book, Catalog, DVD, software
import pickle
# imports


menu = """
    Library Catalog Menu

    1. Search Catalog
    2. Print the entire catalog
    3. Add item to catalog
    4. Remove item from catalog 
    5. Save your catalog

    Choose an option
           """
item_list = """
    Choose a type of item to create
    
    1. DVD
    2. Book 
    3. Software
        """
creation_loop = True
while creation_loop:
    user_input = str(input('would you like to load an existing Catalog or create a new one? "Create"/"Load": '))
    if user_input == 'Load':
        file_to_save_or_load = str(input('name of the file: '))
        try:
            pickle_in = open(file_to_save_or_load, 'rb')
            cat = pickle.load(pickle_in)
            creation_loop = False
        except Exception:
            print('that file does not exist')

    else:
        file_to_save_or_load = str(input('enter name here: '))
        cat = Catalog(file_to_save_or_load)
        creation_loop = False


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

    if user_input == 1:  # searches based on user input
        search_results = cat.search_library(input('input search term here: '))
        print(*search_results)
    elif user_input == 2:  # prints whole catalog
        cat.print_whole()
    elif user_input == 3:  # creates and adds items based on user input
        if display_item_type() == 1:
            item_to_add = DVD.create_DVD()
        elif display_item_type() == 2:
            item_to_add = Book.create_book()
        else:
            item_to_add = software.create_software()
        cat.add_item(item_to_add)
    elif user_input == 4:  # removes an item based on user input
        cat.remove_item(input('name of item: '))
    elif user_input == 5:
        pickle_out = open(file_to_save_or_load, 'wb')
        pickle.dump(cat, pickle_out)
        pickle_out.close()
user_input = display_menu()