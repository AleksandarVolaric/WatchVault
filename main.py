from validation import (
    get_non_empty_text, 
    get_menu_choice,
)

from api import (
    search_titles,
)

# Movie Tracker

# MAIN MENU

# 1. Search for movie / series   (search flow)
#    - Show numbered results
#    - Select result
#    - Show details
#    - Later: confirm and add to library

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

    choice = get_menu_choice(
        "Choose a result: ",
        1,
        len(results),
    )
    selected_result = results[choice - 1]
    selected_id = selected_result["id"]
    ...



# FUTURE LIBRARY FLOW
def library_menu():
    ...


# MAIN
def main():
    while True:
        print("\n--- WatchVault ---")
        print("1. Search for a movie or series")
        print("2. Exit")
        choice = get_menu_choice("Enter your choice (1 or 2): ", 1, 2)

        if choice == 1:
            search_title_flow()
        elif choice == 2:
            print("Exiting the program. Goodbye!")
            break


# keep rotating until ends


if __name__ == "__main__":
    main()
