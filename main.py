from validation import (
    get_non_empty_text, 
    get_menu_choice,
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
    return search_input

# Call API to search for movies
# Check if it returns results
# Display results
# User chooses the result


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
