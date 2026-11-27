# WatchVault

WatchVault is a Python command-line learning project for searching movies and TV series with the TMDB API and managing a personal library in a local SQLite database.

**Current version: v0.5.0**

The main learning focus of v0.5.0 is relational database design: **many-to-many relationships, foreign keys, junction tables, SQL JOINs, and genre filtering**.

## Features

### TMDB Search

- Search for movies and TV series through TMDB.
- Display numbered search results with title, year, and media type.
- Select a result and request detailed information using its TMDB ID.
- Display genres, TMDB rating, overview, runtime for movies, and season count for series.
- Handle missing dates, empty results, timeouts, network errors, and HTTP/API errors.

### Local Library

- Save selected titles to a persistent SQLite database.
- Prevent duplicate titles using TMDB ID and media type.
- View all saved titles.
- Store personal watch status, favorite state, and personal rating.
- Display locally stored genres for saved titles.

**Movie statuses**
- Plan to Watch
- Completed
- Dropped

**Series statuses**
- Plan to Watch
- Watching
- Completed
- Dropped

Personal ratings use a **1–10** scale and are available only for `Completed` or `Dropped` titles.

Changing a title back to `Plan to Watch`, or a series to `Watching`, clears its existing personal rating.

### Genre Filtering

Genres from TMDB are stored locally using a many-to-many relationship:

```text
titles
   ↕
title_genres
   ↕
genres
```

A title can have multiple genres, while the same genre can belong to multiple titles.

The library can be filtered by its locally stored genres:

```text
--- My Library ---

1. View All Titles
2. Filter By Genre
3. Back
```

For example:

```text
--- Action ---

1. Captain America: Civil War (2016) [Movie] Completed
```

Genre retrieval and filtering use SQL `JOIN` queries rather than making additional TMDB requests.

## Database

The SQLite database contains three tables:

### `titles`

Stores saved movies and series together with personal tracking data.

```text
id
tmdb_id
title
media_type
release_year
status
favorite
personal_rating
```

### `genres`

Stores genres received from TMDB.

```text
id
tmdb_id
name
```

TMDB genre IDs are unique, preventing duplicate genre rows.

### `title_genres`

Junction table connecting titles and genres.

```text
title_id
genre_id
```

`title_id` and `genre_id` are foreign keys. Together they form a composite primary key, preventing duplicate title-genre relationships.

Foreign-key enforcement is enabled for every SQLite connection.

## Technologies

- Python
- SQLite and Python's built-in `sqlite3`
- TMDB API
- `requests`
- `python-dotenv`
- SQL including `SELECT`, `INSERT`, `INSERT OR IGNORE`, `UPDATE`, `WHERE`, `JOIN`, `ORDER BY`, foreign keys, composite primary keys, and `UNIQUE` constraints

## Project Structure

```text
.
├── api.py          # TMDB API communication
├── database.py     # SQLite queries and database operations
├── main.py         # CLI and application flow
├── schema.sql      # Relational database schema
├── validation.py   # Reusable input validation
├── tests/          # Reserved for future automated tests
├── .env            # Local TMDB token; not committed
├── watchvault.db   # Generated local database; not committed
└── .gitignore
```

## Setup

Install the dependencies:

`python -m pip install requests python-dotenv`

Create a `.env` file in the project root:

`TMDB_TOKEN=your_token`

Replace `your_token` with your TMDB API Read Access Token.

**Never commit your real TMDB token.**

## Run

From the project root:

`python main.py`

The main menu provides:

```text
--- WatchVault ---

1. Search for a movie or series
2. My Library
3. Exit
```

Search results can be opened for detailed TMDB information and added to the local library.

Inside **My Library**, titles can be managed or filtered by genre.

## Short Roadmap

Future goals include:

- Series progress tracking
- Library search, filtering, and additional views
- External TMDB metadata refreshing
- JSON backup and import
- Automated testing, cleanup, documentation, and a v1.0 release