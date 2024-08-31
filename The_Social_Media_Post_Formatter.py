def stylized_post(post_string):
    stylized_chars = []
    for char in post_string:
        if char == "a":
            stylized_chars.append('@')
        elif char == "e":
            stylized_chars.append('3')
        else:
            stylized_chars.append(char)
    return ''.join(stylized_chars)

while True:
    user_post = input("Enter your social media post: ")
    stylized_post = stylized_post(user_post)

    print(f"Stylized post: {stylized_post}")

    continue_input = input("Would you like to stylize another post? (yes/no): ").lower()
    if continue_input != "yes":
        break