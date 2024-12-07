from pymongo import MongoClient

def get_db_connection():
    client = MongoClient(
        host='localhost',
        port=27017,
        username='',
        password='',
        authSource='admin'
    )
    db = client['login']  # Your database name
    return db
