import pg8000

try:
    conn = pg8000.connect(
        host="localhost",
        port=5432,
        database="wineshop",
        user="postgres",
        password="postgres"
    )

    print("SUCCESS: Connected to PostgreSQL")

    cursor = conn.cursor()
    cursor.execute("SELECT version();")

    row = cursor.fetchone()
    print(row)

    conn.close()

except Exception as e:
    print("FAILED")
    print(e)