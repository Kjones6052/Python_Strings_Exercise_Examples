def create_welcome_message(name):
    line_length = 30
    center_name = name.center(line_length, '*')
    return f"Welcome {center_name} Welcome"

while True:
    user_name = input("Please enter your name for a personalized welcome message: ")
    if user_name.isalpha():
        welcome_message = create_welcome_message(user_name)
        print(welcome_message)
    else:
        print("Invalid name, please enter alphabetic characters only.")
    
    continue_input = input("Would you like to create another welcome message? (yes/no): ").lower()
    if continue_input != "yes":
        break