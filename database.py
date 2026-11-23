import sqlite3


def init_db():
    with open("schema.sql", "r", encoding="utf-8") as file:
        schema = file.read()
    with sqlite3.connect("watchvault.db") as connection:
        connection.executescript(schema)


def add_title(tmdb_id, title, media_type, release_year):
    try:
        with sqlite3.connect("watchvault.db") as connection:
            connection.execute(
                """
                INSERT INTO titles(tmdb_id, title, media_type, release_year)
                VALUES (?, ?, ?, ?)
                """,
                (tmdb_id, title, media_type, release_year),
            )
        return True
    
    except sqlite3.IntegrityError:
        return False


def get_all_titles():
    with sqlite3.connect("watchvault.db") as connection:
        cursor = connection.execute(
            """
            SELECT id, tmdb_id, title, media_type, release_year
            FROM titles
            ORDER BY title
            """
        )
        rows = cursor.fetchall()
        return rows