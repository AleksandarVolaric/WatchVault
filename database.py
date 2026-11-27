import sqlite3

def get_connection():
    connection = sqlite3.connect("watchvault.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def init_db():
    with open("schema.sql", "r", encoding="utf-8") as file:
        schema = file.read()
    with get_connection() as connection:
        connection.executescript(schema)


def add_title(tmdb_id, title, media_type, release_year):
    try:
        with get_connection() as connection:
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
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT 
                id, 
                tmdb_id, 
                title, 
                media_type, 
                release_year, 
                status, 
                favorite, 
                personal_rating
            FROM titles
            ORDER BY title
            """
        )
        rows = cursor.fetchall()
        return rows



def update_status(title_id, status):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE titles
            SET status = ?
            WHERE id = ?
            """,
            (status, title_id)
        )


def update_favorite(title_id, favorite):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE titles
            SET favorite = ?
            WHERE id = ?
            """,
            (favorite, title_id)
        )


def update_rating(title_id, rating):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE titles
            SET personal_rating = ?
            WHERE id = ?
            """,
            (rating, title_id)
        )


def add_genre(tmdb_id, name):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT OR IGNORE INTO genres (tmdb_id, name)
            VALUES (?, ?)
            """,
            (tmdb_id, name)
        )


def get_genre_id(tmdb_id):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id
            FROM genres
            WHERE tmdb_id = ?
            """,
            (tmdb_id,)
        )
        row = cursor.fetchone()
        return row[0]


def add_title_genre(title_id, genre_id):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT OR IGNORE INTO title_genres (title_id, genre_id)
            VALUES (?, ?)
            """,
            (title_id, genre_id)
        )


def get_title_id(tmdb_id, media_type):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id
            FROM titles
            WHERE tmdb_id = ?
            and media_type = ?
            """,
            (tmdb_id, media_type)
        )
        row = cursor.fetchone()
        return row[0]


def get_title_genres(title_id):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT genres.name
            FROM title_genres
            JOIN genres
                ON title_genres.genre_id = genres.id
            WHERE title_genres.title_id = ?
            """,
            (title_id,)
        )
        rows = cursor.fetchall()

        genre_names = []
        for row in rows:
            genre_names.append(row[0])

        return genre_names


def get_all_genres():
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id, name
            FROM genres
            ORDER BY name
            """
        )
        rows = cursor.fetchall()
        return rows


def get_titles_by_genre(genre_id):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT
                titles.id,
                titles.title,
                titles.media_type,
                titles.release_year,
                titles.status,
                titles.favorite,
                titles.personal_rating
            FROM titles
            JOIN title_genres
                ON titles.id = title_genres.title_id
            WHERE title_genres.genre_id = ?
            """,
            (genre_id,)
        )
        rows = cursor.fetchall()
        return rows