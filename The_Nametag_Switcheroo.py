def swap_characters(user_name):
    if len(user_name) > 1:
        return user_name[-1] + user_name[1:-1] + user_name[0]
    else:
        return user_name

while True:
    username_input = input("Enter your user name to see the magic swap: ")
    swapped_username = swap_characters(username_input)

    print(f"Ta da! Your magical username in: {swapped_username}")

    continue_input = input("Want to try another username? (yes/no): ").lower()
    if continue_input != "yes":
        break