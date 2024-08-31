def format_highlights(highlight_string):
    if highlight_string.strip():
        return [play.strip() for play in highlight_string.split(',')]
    else:
        return []
    
while True:
    user_input = input("Enter the game highlights, separated by commas: ")
    formatted_highlights = format_highlights(user_input)

    if formatted_highlights:
        print("Game highlights: ")
        for play in formatted_highlights:
            print(f"- {play}")
    else:
        print("No highlights entered, please provide highlights of the game.")
    
    continue_input = input("Do you want to enter more highlights? (yes/no): ").lower()
    if continue_input != "yes":
        break