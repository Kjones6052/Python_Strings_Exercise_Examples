def print_stats(stats_string):
    stats_list = stats_string.split(';')
    for stat in stats_list:
        category_value = stat.split(':')
        if len(category_value) == 2:
            category, value = category_value
            print(f" Category: {category}, Value: {value}")
        else:
            print(f"Invalid format for stat: {stat}")
            break

while True:
    stats_input = input("Enter your stats separated by semicolons (e.g. Goals:4;Assists:2;Fouls:1): ")
    print_stats(stats_input)

    continue_input = input("Would you like to enter more stats? (yes/no): ")
    if continue_input != "yes":
        break