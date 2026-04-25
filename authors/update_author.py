from database import get_connection

def update_author():
    conn = get_connection()
    cursor = conn.cursor()

    ID = int(input("Enter the ID you want to update: "))

    cursor.execute("SELECT * FROM authors WHERE id = ?", (ID,))
    row = cursor.fetchone()
    if row is None:
        print("Author not found")
        conn.close()
        return

    name = input("New name (leave empty to keep current): ")
    if name == "" :
        name = row[1]
    birth_date = (input("New date (leave empty to keep current): "))
    if birth_date == "" :
        birth_date = row[2]
    nationality = input("New nationality (leave empty to keep current): ")
    if nationality == "" :
        nationality = row[3]
    description = input("New description (leave empty to keep current): ")
    if description == "" :
        description = row[4]

    cursor.execute("""
    UPDATE authors 
    SET name = ?, birth_date = ?, nationality = ?, description = ? 
    WHERE id = ? 
    """, (name, birth_date, nationality, description, ID))

    conn.commit()
    print("Author updated successfully!")
    conn.close()