# WatchVault

WatchVault is a Python command-line learning project for searching movies and TV series with The Movie Database (TMDB) API. The v0.1.0 learning focus is REST API fundamentals: HTTP requests, JSON responses, query parameters, and environment variables.

## Current features

- Search TMDB for movies and TV series.
- Send HTTP GET requests with `requests` and query parameters, authenticating with the TMDB Read Access Token in the HTTP Authorization header.
- Parse the JSON response and filter results to movies and TV series.
- Display numbered results with each title, release year, and media type.
- Show `Unknown` when a result has no release date.
- Let the user select a result and extract its TMDB ID.
- Handle searches with no results and basic timeout, network, and HTTP/API errors.
- Validate non-empty search input and numbered menu choices.

## Technologies used

- Python
- [The Movie Database (TMDB) API](https://developer.themoviedb.org/docs)
- `requests` for HTTP requests
- `python-dotenv` for loading environment variables from `.env`

## Project structure

```text
.
├── api.py          # TMDB search request and response handling
├── main.py         # Command-line menu and search flow
├── validation.py   # CLI input validation
├── tests/          # Project tests
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

Choose the search option, enter a movie or series title, and select a result by its displayed number.

## Current project status / version

WatchVault is an early-stage learning and portfolio project. **Current version: v0.1.0.** The current CLI supports searching and selecting a TMDB result; a persistent personal library is not part of this version.

## Short roadmap

Future goals include:

- Detailed TMDB title information
- A local SQLite library
- Personal watch tracking
- Genres and series progress
- Library search and filtering
- Metadata refreshing
- JSON backup and import
- Testing and a v1.0 release
