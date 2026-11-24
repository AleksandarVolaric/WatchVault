# WatchVault

WatchVault is a Python command-line learning project for searching movies and TV series with The Movie Database (TMDB) API and saving selected titles to a local SQLite database. In v0.4.0, the learning focus is personal watch tracking, editable user-owned data, and SQL `UPDATE` operations.

## Current features

- Search TMDB for movies and TV series.
- Send HTTP GET requests with `requests`, query parameters for search, and Bearer token authentication.
- Parse search JSON and filter results to movies and TV series.
- Display numbered search results with each title, release year, and media type.
- Select a result and use its TMDB ID and media type to request detailed information.
- Movies use TMDB's `/movie/{id}` endpoint; TV series use `/tv/{id}`.
- Display title, release or first-air year, type, genres, TMDB rating, overview, and runtime or number of seasons.
- Handle missing dates, empty results, timeouts, network errors, and HTTP/API errors.
- Validate non-empty text, numbered menu choices, and personal ratings.
- Save selected movies and series to a persistent local SQLite library.
- Prevent duplicate library entries using the TMDB ID and media type.
- View all locally saved titles.
- Manage individual saved titles from the library.

### Personal tracking

Each saved title can now store personal tracking data.

**Movies**
- Plan to Watch
- Completed
- Dropped

**TV series**
- Plan to Watch
- Watching
- Completed
- Dropped

Both movies and series support:

- Favorite: Yes / No
- Personal rating from 1–10
- Editing the current status
- Toggling favorite status
- Updating the personal rating

Personal ratings are only allowed for titles with a status of `Completed` or `Dropped`.

If a title is changed back to `Plan to Watch`, or a series is changed to `Watching`, its existing personal rating is cleared because the rating is no longer valid for that status.

## Technologies used

- Python
- SQLite for local persistent storage
- Python's built-in `sqlite3` module for database access
- [The Movie Database (TMDB) API](https://developer.themoviedb.org/docs)
- `requests` for HTTP requests
- `python-dotenv` for loading environment variables from `.env`

## Project structure

```text
.
├── api.py          # TMDB search and title-detail requests
├── database.py     # SQLite initialization, queries, inserts, and updates
├── main.py         # CLI flow, TMDB search, library, and personal tracking
├── schema.sql      # SQLite database schema
├── validation.py   # CLI input and personal-rating validation
├── tests/          # Reserved for future automated tests
├── .env            # Local TMDB token; create this file yourself
├── watchvault.db   # Generated local SQLite database; ignored by Git
└── .gitignore      # Keeps local secrets and database files out of Git
```

## Local database

The `titles` table currently stores:

- Local database ID
- TMDB ID
- Title
- Media type
- Release year
- Personal watch status
- Favorite state
- Personal rating

New titles start with:

- Status: `Plan to Watch`
- Favorite: `No`
- Personal rating: `Not rated`

The combination of TMDB ID and media type is unique, preventing the same TMDB title from being added twice.

## Setup

1. Install the dependencies:

   ```bash
   python -m pip install requests python-dotenv
   ```

2. Create a `.env` file in the project root.

3. Add your TMDB API Read Access Token:

   ```dotenv
   TMDB_TOKEN=their_token
   ```

   Replace `their_token` with your own token.

   The `.env` file is ignored by Git. **Never commit your real TMDB token.**

## How to run

From the project root:

```bash
python main.py
```

From the main menu you can:

1. Search for a movie or series
2. Open My Library
3. Exit

After selecting a TMDB search result, choose **Add to Library** to save it locally.

Inside **My Library**, select a saved title to:

1. Change Status
2. Toggle Favorite