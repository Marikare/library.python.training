def menu_authors():
    from .create_author import create_author
    from .list_authors import list_authors
    from .update_author import update_author
    from .delete_author import delete_author
    
    while True:
        print("""
        1. Create Author
        2. List Authors
        3. Update Author
        4. Delete Author
        0. Back
        """.strip())

        option = input("Choose an option: ")
        if option == "1":
            create_author()
        elif option == "2":
            list_authors()
        elif option == "3":
            update_author()
        elif option == "4":
            delete_author()
        elif option == "0":
            break
        else:
            print("Invalid option, try again.")
