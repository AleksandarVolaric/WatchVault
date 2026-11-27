from validation import (
    get_non_empty_text, 
    get_menu_choice,
    get_rating,
)

from api import (
    search_titles,
    get_title_details,
)

from database import (
    init_db,
    add_title,
    get_all_titles,
    update_status,
    update_favorite,
    update_rating,
    add_genre,
    get_genre_id,
    add_title_genre,
    get_title_id,
    get_title_genres,
    get_all_genres,
    get_titles_by_genre,
)

STATUS_LABELS = {
    "plan_to_watch": "Plan to Watch",
    "watching": "Watching",
    "completed": "Completed",
    "dropped": "Dropped",
}



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
            title_id = get_title_id(selected_id, selected_media_type)

            for genre in genres:
                genre_tmdb_id = genre["id"]
                genre_name = genre["name"]
                add_genre(genre_tmdb_id, genre_name)
                genre_id = get_genre_id(genre_tmdb_id)
                add_title_genre(title_id, genre_id)

            print(f"{title} was added to your library.")
        else:
            print(f"{title} is already in your library.")

    elif choice == 2:
        return


# LIBRARY FLOW
def filter_by_genre():
    genres = get_all_genres()

    if not genres:
        print("\nNo genres are available in your library.")
        return

    print("\n--- Filter by Genre ---")

    for number, genre in enumerate(genres, start=1):
        genre_id, genre_name = genre
        print(f"{number}. {genre_name}")

    genre_choice = get_menu_choice("Choose a genre: ", 1, len(genres))
    selected_genre = genres[genre_choice - 1]
    selected_genre_id, selected_genre_name = selected_genre
    filtered_titles = get_titles_by_genre(selected_genre_id)
    
    if not filtered_titles:
        print(f"\nNo titles found for {selected_genre_name}.")
        return

    print(f"\n--- {selected_genre_name} ---")

    for number, row in enumerate(filtered_titles, start=1):
        (
            title_id,
            title,
            media_type,
            release_year,
            status,
            favorite,
            personal_rating,
        ) = row

        if media_type == "movie":
            display_type = "Movie"
        else:
            display_type = "Series"

        if release_year is None:
            display_year = "Unknown"
        else:
            display_year = release_year

        display_status = STATUS_LABELS[status]

        print(
            f"{number}. {title} ({display_year}) "
            f"[{display_type}] {display_status}"
        )


def view_all_titles():
    titles = get_all_titles()
    if not titles:
        print("\nYour library is empty.")
        return

    print("\n--- My Library ---")

    for number, row in enumerate(titles, start=1):
        (
            id, 
            tmdb_id, 
            name, 
            media_type, 
            release_year, 
            status, 
            favorite, 
            personal_rating,
        ) = row

        if media_type == "movie":
            display_type = "Movie"
        else:
            display_type = "Series"

        if release_year is None:
            display_year = "Unknown"
        else:
            display_year = release_year

        display_status = STATUS_LABELS[status]

        print(f"{number}. {name} ({display_year}) [{display_type}] {display_status}")


    choice = get_menu_choice("Choose a title: ", 1, len(titles))
    selected_title = titles[choice - 1]
    (
        selected_id,
        selected_tmdb_id,
        selected_name,
        selected_media_type,
        selected_release_year,
        selected_status,
        selected_favorite,
        selected_rating,
) = selected_title

    selected_genres = get_title_genres(selected_id)
    display_genres = ", ".join(selected_genres)
    display_status = STATUS_LABELS[selected_status]

    if selected_favorite == 1:
        display_favorite = "Yes"
    else:
        display_favorite = "No"

    if selected_rating is None:
        display_rating = "Not rated"
    else:
        display_rating = f"{selected_rating}/10"

    print(f"\n--- {selected_name} ---")
    print(f"Status: {display_status}")
    print(f"Favorite: {display_favorite}")
    print(f"Personal Rating: {display_rating}")
    print(f"Genres: {display_genres}")

    print("\n1. Change Status")
    print("2. Toggle Favorite")
    print("3. Set Rating")
    print("4. Back")

    action_choice = get_menu_choice("Choose an action: ", 1, 4)

    if action_choice == 1:
        if selected_media_type == "movie":
            statuses = ["plan_to_watch", "completed", "dropped"]

        elif selected_media_type == "tv":
            statuses = ["plan_to_watch", "watching", "completed", "dropped"]

        print("\n--- Change Status ---")
        for number, status in enumerate(statuses, start=1):
            print(f"{number}. {STATUS_LABELS[status]}")

        status_choice = get_menu_choice("Choose a status: ", 1, len(statuses))
        selected_status = statuses[status_choice - 1]
        update_status(selected_id, selected_status)

        if selected_status == "plan_to_watch" or selected_status == "watching":
            update_rating(selected_id, None)

    elif action_choice == 2:
        if selected_favorite == 0:
            new_favorite = 1
        else:
            new_favorite = 0
        update_favorite(selected_id, new_favorite)

    elif action_choice == 3:
        if selected_status == "completed" or selected_status == "dropped":
            new_rating = get_rating("Enter your rating (1-10): ")
            update_rating(selected_id, new_rating)
        else:
            print("You can only rate titles that are Completed or Dropped.")

    elif action_choice == 4:
        return 


def library_menu():
    print("\n--- My Library ---")
    print("1. View All Titles")
    print("2. Filter By Genre")
    print("3. Back")

    choice = get_menu_choice("Choose an option: ", 1, 3)

    if choice == 1:
        view_all_titles()

    elif choice == 2:
        filter_by_genre()

    elif choice == 3:
        return
# 2. My Library
# - View all titles        +
# - Edit status            +
# - Toggle favorite        +
# - Set personal rating    +
# - Filter by genre        +
#
# Later:
# - Search my library
# - Filter by status
# - Favorites view
# - Movies only
# - Series only

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
