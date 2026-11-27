CREATE TABLE IF NOT EXISTS titles (
    id INTEGER PRIMARY KEY,
    tmdb_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    media_type TEXT NOT NULL,
    release_year INTEGER,
    status TEXT NOT NULL DEFAULT 'plan_to_watch',
    favorite INTEGER NOT NULL DEFAULT 0,
    personal_rating INTEGER,
    UNIQUE (tmdb_id, media_type)
);


CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY,
    tmdb_id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS title_genres (
    title_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (title_id, genre_id),
    FOREIGN KEY (title_id) REFERENCES titles(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);