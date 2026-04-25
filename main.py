from database import create_tables
from authors.menu_authors import menu_authors

def main():

    create_tables()
    
    while True:
        print("""
        1. Authors Menu
        0. Exit
        """.strip())

        option = input("Choose an option: ")
        if option == "1":
            menu_authors()
        elif option == "0":
            break
        else:
            print("Invalid option, try again.")