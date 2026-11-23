# WatchVault

WatchVault is a Python command-line learning project for searching movies and TV series with The Movie Database (TMDB) API. In v0.2.0, the learning focus is using data from one REST API request (the selected TMDB ID and media type) to make a second request to the appropriate movie or TV endpoint.

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

## Technologies used

- Python
- [The Movie Database (TMDB) API](https://developer.themoviedb.org/docs)
- `requests` for HTTP requests
- `python-dotenv` for loading environment variables from `.env`

## Project structure

```text
.
├── api.py          # TMDB search and title-detail requests
├── main.py         # Command-line menu, search, and title details
├── validation.py   # CLI input validation
├── tests/          # Reserved for future automated tests
├── .env            # Local TMDB token; create this file yourself
└── .gitignore      # Keeps .env and other local files out of Git
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

Choose the search option, enter a movie or series title, and select a result by its displayed number to view its TMDB details.

## Current project status / version

WatchVault is an early-stage learning and portfolio project. **Current version: v0.2.0.** The CLI supports searching, selecting a TMDB result, and viewing its details. The displayed “Add to Library” option is a placeholder; this version does not save a library.

## Short roadmap

Future goals include:

- v0.3.0: A local SQLite library
- Personal watch tracking
- Genres and series progress
- Library search and filtering
- Metadata refreshing
- JSON backup and import
- Testing and a v1.0 release
