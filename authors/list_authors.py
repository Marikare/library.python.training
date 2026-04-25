from database import get_connection

def list_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors")

    rows = cursor.fetchall()
    for row in rows:
        print(f"""
        ID: {row[0]}
        Name: {row[1]}
        Date of Birth: {row[2]}
        Nationality: {row[3]}
        Description: {row[4]}
        """)
 
    conn.close()