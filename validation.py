# VALIDATION CHECKS



def get_non_empty_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text

        print("Input cannot be empty. Please try again.")


def get_menu_choice(prompt, min_choice, max_choice):
    while True:
        choice = input(prompt).strip()
        if choice.isdigit():
            choice_int = int(choice)
            if min_choice <= choice_int <= max_choice:
                return choice_int

        print(
            f"Invalid choice. Please enter a number between "
            f"{min_choice} and {max_choice}."
        )






# LATER
# Rating int 1-10
# Proper number for searies or seasons