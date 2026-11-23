import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

def search_titles(search_text):
    url = "https://api.themoviedb.org/3/search/multi"

    headers = {
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    params = {
        "query": search_text
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

    except requests.exceptions.Timeout:
        print("The request timed out")
        return[]
    
    except requests.exceptions.RequestException:
        print("A network or API error occurred.")
        return []

    data = response.json()

    results = data["results"]

    filtered_results = []
    for result in results:
        if result["media_type"] == "movie" or result["media_type"] == "tv":
            filtered_results.append(result)
    return filtered_results


def get_title_details(selected_id, selected_media_type):
    if selected_media_type == "movie":
        url = f"https://api.themoviedb.org/3/movie/{selected_id}"
    elif selected_media_type == "tv":
        url = f"https://api.themoviedb.org/3/tv/{selected_id}"

    headers = {
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

    except requests.exceptions.Timeout:
        print("The request timed out.")
        return None

    except requests.exceptions.RequestException:
        print("A network or API error occurred.")
        return None

    data = response.json()
    return data