from database import get_connection

def delete_author():
    conn = get_connection()
    cursor = conn.cursor()

    ID = int(input("Enter the ID you want to delete: "))

    cursor.execute("SELECT * FROM authors WHERE id = ?", (ID,))
    row = cursor.fetchone()
    if row is None:
        print("Author not found")
        conn.close()
        return
    cursor.execute("DELETE FROM authors WHERE id = ?", (ID,))
    
    conn.commit()
    print("Author deleted successfully!")
    conn.close()