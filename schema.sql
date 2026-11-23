CREATE TABLE IF NOT EXISTS titles (
    id INTEGER PRIMARY KEY,
    tmdb_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    media_type TEXT NOT NULL,
    release_year INTEGER,
    UNIQUE (tmdb_id, media_type)
);