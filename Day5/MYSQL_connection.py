
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="MYSQL",
        database="Prod_db",
        use_pure=True
    )

    print("Database connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prod")

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found in the prod table.")

    cursor.close()
    conn.close()

    print("Database connection closed.")

except mysql.connector.Error as err:
    print("Database error:", err)
