import psycopg2

def connect_to_postgres(host, user, password, database, port=3030):
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        conn.autocommit = True  # For simplicity, autocommit is set to True
        print("Connected to PostgreSQL database successfully!")
        return conn
    except psycopg2.Error as err:
        print(f"Error connecting to PostgreSQL database: {err}")
        return None

# Replace with secure credential management (e.g., environment variables, config files)
host = "localhost"  # This should be your hostname
port = 3030  # PostgreSQL port
user = "postgres"  # Replace with your actual username
password = "root"  # Replace with your actual password
database = "practice"  # Your database name

conn = connect_to_postgres(host, user, password, database, port)

if conn:
    try:
        cursor = conn.cursor()
        # Perform database operations using the cursor
        # Example:
        cursor.execute("SELECT * FROM course")  # Replace 'your_table' with the actual table name
        result = cursor.fetchall()
        for row in result:
            print(row)
    except psycopg2.Error as err:
        print(f"Error executing query: {err}")
    finally:
        cursor.close()
        conn.close()
