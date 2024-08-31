def reverse_agenda(agenda_string):
    agenda_items = agenda_string.split(', ')
    reversed_agenda = agenda_items[::-1]
    return ', '.join(reversed_agenda)

while True:
    user_agenda = input("Enter your meeting agenda items separated by commas: ")
    reverse_order = reverse_agenda(user_agenda)
    print(f"Reverse agenda order: {reverse_order}")

    continue_input = input("Would you like to reverse another agenda? (yes/no): ").lower()
    if continue_input != "yes":
        break