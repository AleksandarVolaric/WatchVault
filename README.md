# WatchVault

WatchVault is a Python command-line learning project for searching movies and TV series with The Movie Database (TMDB) API and saving selected titles to a local SQLite database. In v0.3.0, the learning focus is connecting external API data to persistent local storage.

## Current features

- Search TMDB for movies and TV series.
- Send HTTP GET requests with `requests`, query parameters for search, and Bearer token authentication.
- Parse search JSON and filter results to movies and TV series.
- Display numbered search results with each title, release year, and media type.
- Let the user select a result, then use its TMDB ID and media type to request title details. Movies use TMDB's `/movie/{id}` endpoint; TV series use `/tv/{id}`.
- Display the selected title's name, release or first-air year, type, genres, TMDB rating (to one decimal place), and overview. Show `Unknown` when its date is missing.
- Display runtime for movies or the number of seasons for TV series.
- Handle searches with no results and basic timeout, network, and HTTP/API request errors.
- Validate non-empty search input and numbered menu choices.
- Initialize a local SQLite database when the application starts.
- Add the selected movie or series to the local library and view saved titles from the CLI.
- Store each title's local ID, TMDB ID, title, media type, and release year. A TMDB ID and media type combination can only be saved once; duplicate additions are reported without crashing.
- Use parameterized SQL for title inserts.

## Technologies used

- Python
- SQLite for local persistent storage
- Python's built-in `sqlite3` module for SQLite database access
- [The Movie Database (TMDB) API](https://developer.themoviedb.org/docs)
- `requests` for HTTP requests
- `python-dotenv` for loading environment variables from `.env`

## Project structure

```text
.
├── api.py          # TMDB search and title-detail requests
├── database.py     # SQLite initialization and title operations
├── main.py         # Command-line menu, search, title details, and library
├── schema.sql      # SQLite titles table definition
├── validation.py   # CLI input validation
├── tests/          # Reserved for future automated tests
├── .env            # Local TMDB token; create this file yourself
├── watchvault.db   # Generated local SQLite database; ignored by Git
└── .gitignore      # Keeps local secrets and database files out of Git
```

## Setup

1. Install the dependencies:

   ```bash
   python -m pip install requests python-dotenv
   ```

2. Create a `.env` file in the project root.

3. Add your TMDB API Read Access Token to `.env`:

   ```dotenv
   TMDB_TOKEN=their_token
   ```

   Replace `their_token` with your own token. The `.env` file is ignored by Git; **never commit your real token**.

## How to run

From the project root, run:

```bash
python main.py
```

Choose the search option, enter a movie or series title, and select a result by its displayed number to view its TMDB details. Choose **Add to Library** to save it locally. Use **My Library** from the main menu to list saved titles. The database is created as `watchvault.db` in the project directory and is ignored by Git.

## Current project status / version

WatchVault is an early-stage learning and portfolio project. **Current version: v0.3.0.** The CLI supports searching TMDB, viewing selected title details, and saving and listing titles in a local SQLite library.

## Short roadmap

Future goals include:

- v0.4.0: Personal tracking with watch status, favorites, and personal ratings
- Genres and series progress
- Library search and filtering
- Metadata refreshing
- JSON backup and import
- Testing and a v1.0 release
