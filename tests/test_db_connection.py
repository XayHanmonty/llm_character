from core.db.mongodb import connection


def test_database_connection():
    """Tests the MongoDB database connection."""
    print("Testing database connection...")
    db = connection.get_database()
    assert db is not None, "Database object should not be None"
    print(f"Database: {db.name}")
    collections = db.list_collection_names()
    print("Collections:", collections)
    assert isinstance(collections, list), "list_collection_names should return a list"
    connection.close()
    print("Database connection test successful.")
