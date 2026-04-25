from database import get_connection

def create_author():
    name = input("Enter the author's name: ")
    birth_date = input("Enter the author's date of birth: ")
    nationality = input("Enter the author's nationality: ")
    description = input("Enter the author's description (optional): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    insert into authors (name, birth_date, nationality, description)
    VALUES (?, ?, ?, ?)
    """, (name, birth_date, nationality, description))

    conn.commit()
    print("Author created successfully!")
    conn.close()