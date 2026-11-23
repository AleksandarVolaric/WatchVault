from validation import (
    get_non_empty_text, 
    get_menu_choice,
)

from api import (
    search_titles,
    get_title_details,
)

from database import (
    init_db,
    add_title,
    get_all_titles,
)



# SEARCH FLOW
def search_title_flow():
    search_input = get_non_empty_text(
        "Enter the title of the movie or series to search: "
    )

    results = search_titles(search_input)

    if not results:
        print("No movies or Series found")
        return    
    
    for number, result in enumerate(results, start=1):
        if result["media_type"] == "movie":
            name = result["title"]
            date = result["release_date"]
            display_type = "Movie"
        else:
            name = result["name"]
            date = result["first_air_date"]
            display_type = "Series"
        if date:
            year = date[:4]
        else:
            year = "Unknown"

        print(f"{number}. {name} ({year}) [{display_type}]")

    choice = get_menu_choice("Choose a result: ", 1, len(results))
    selected_result = results[choice - 1]
    selected_id = selected_result["id"]
    selected_media_type = selected_result["media_type"]

    details = get_title_details(selected_id, selected_media_type)

    if not details:
        return

    if selected_media_type == "movie":
        title = details["title"]
        date = details["release_date"]
        runtime = details["runtime"]
        display_type = "Movie"
    elif selected_media_type == "tv":
        title = details["name"]
        date = details["first_air_date"]
        seasons = details["number_of_seasons"]
        display_type = "Series"
    if date:
        release_year = int(date[:4])
        display_year = date[:4]
    else:
        release_year = None
        display_year = "Unknown"
    overview = details["overview"]
    rating = details["vote_average"]
    genres = details["genres"]

    genre_names = []
    for genre in genres:
        genre_names.append(genre["name"])
    genres_text = ", ".join(genre_names)

    print("\n--- Title Details ---")
    print(f"{title} ({display_year}) [{display_type}]")
    print(f"Genres: {genres_text}")
    if selected_media_type == "movie":
        print(f"Runtime: {runtime} minutes")
    elif selected_media_type == "tv":
        print(f"Seasons: {seasons}")
    print(f"TMDB Rating: {rating:.1f}/10")
    print("\nOverview:")
    print(overview)
    print("\n1. Add to Library")
    print("2. Back")

    choice = get_menu_choice("Enter your choice (1 or 2): ", 1, 2)
    if choice == 1:
        added = add_title(selected_id, title, selected_media_type, release_year)
        if added:
            print(f"{title} was added to your library.")
        else:
            print(f"{title} is already in your library.")

    elif choice == 2:
        return


# LIBRARY FLOW
def library_menu():
    titles = get_all_titles()
    if not titles:
        print("\nYour library is empty.")
        return

    print("\n--- My Library ---")

    for row in titles:
        id, tmdb_id, name, media_type, release_year = row

        if media_type == "movie":
            display_type = "Movie"
        else:
            display_type = "Series"

        if release_year is None:
            display_year = "Unknown"
        else:
            display_year = release_year

        print(f"{id}. {name} ({display_year}) [{display_type}]")



# 2. My Library
#    - View all titles
#    - Search my library
#    - Currently watching
#    - Plan to watch
#    - Completed
#    - Dropped
#    - Favorites
#    - Filter by genre
#    - Movies only
#    - Series only

# 3. Exit



# MAIN
def main():
    init_db()

    while True:
        print("\n--- WatchVault ---")
        print("1. Search for a movie or series")
        print("2. My Library")
        print("3. Exit")
        choice = get_menu_choice("Enter your choice (1, 2 or 3): ", 1, 3)

        if choice == 1:
            search_title_flow()
        elif choice == 2:
            library_menu()
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break



if __name__ == "__main__":
    main()
