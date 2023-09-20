import psycopg2
import os
import dotenv

dotenv.load_dotenv()

postgres_db = os.environ.get('POSTGRES_DB')
postgres_password = os.environ.get('POSTGRES_PASSWORD')

connection = psycopg2.connect(host="localhost", user="postgres", port=5432, database=postgres_db, password=postgres_password)
connection.autocommit = True
cursor = connection.cursor()

# One time process in db_setup.txt is recommended before running this script

cursor.execute("""
    
""")


cursor.close()
connection.close()