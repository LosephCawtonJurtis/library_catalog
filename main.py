from library_catalog import LibraryItem, Book, Catalog

master = Catalog("master", "none", "none")


while True:
    user_input = master.display_menu()

    if user_input == 1:
        print(master.search_library(str(input("item name")), str(input("item type"))))
    elif user_input == 3:
        master.add_item(input("item name"), input("item type"))
    elif user_input == 4:
        master.remove_item(input("item name"), input("item type"))
    elif user_input == 2:
        print(master.item)

user_input = master.display_menu()