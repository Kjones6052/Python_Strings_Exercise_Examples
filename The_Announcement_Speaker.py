def announce_message(message):
    return message.upper()

while True:
    user_input = input("Enter your message for the announcement: ")
    if user_input.strip():
        announcement = announce_message(user_input)
        print(f"Announcement: {announcement}")
    else:
        print("No message entered. Please provide a message for the announcement.")

    continue_input = input("Do you want to make another announcement? (yes/no): ").lower()
    if continue_input != "yes":
        break