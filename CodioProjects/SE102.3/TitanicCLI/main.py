from load_data import load_data

ALL_DATA = load_data()
SHIP_DICTIONARY = ALL_DATA['data']


def print_commands(*_):
    """
    prints all available commands after user typed help.
    """
    print("Available commands:")
    for command in FUNCTION_DICT:
        print(f"{command} {FUNCTION_DICT[command]["parameter"]}")


def print_all_countries_no_duplicates(*_):
    """
    prints a list with all countries ordered alphabetically without duplicates.
    """
    countries_list = [item["COUNTRY"] for item in SHIP_DICTIONARY]
    countries_list_no_duplicates_sorted = sorted(list(set(countries_list)))
    for country in countries_list_no_duplicates_sorted:
        print(country)


def print_top_countries_and_ship_count(amount: str, *_):
    """
    prints the countries with the most ships, where user can enter how many will be printed.
    """
    ships_by_country_dict = get_property_count(SHIP_DICTIONARY, "COUNTRY")
    try:
        amount = abs(int(amount))
    except ValueError:
        print(f"Argument {amount} is not a number")
        return

    sorted_by_value = sorted(ships_by_country_dict.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {amount} countries by ship count:")
    for country, count in sorted_by_value[:amount]:
        print(f"{country}: {count}")


def get_property_count(ships_data: dict, property_name: str) -> dict:
    """
    Gets the count of a given property of a given object as a dictionary.
    """
    ships_by_country_dictionary = dict()
    for info in ships_data:
        property_value = info[property_name]
        if property_value not in ships_by_country_dictionary:
            ships_by_country_dictionary[property_value] = 0
        ships_by_country_dictionary[property_value] += 1
    return ships_by_country_dictionary


def ships_by_types(*_):
    """
    prints every ship type with its corresponding amount.
    """
    ships_by_types_dict = get_property_count(SHIP_DICTIONARY, "TYPE_SUMMARY")
    # print(ships_by_types_dict)
    for ship_type, count in ships_by_types_dict.items():
        print(f"{ship_type}: {count}")


def search_ship(ship_name: str, *_):
    """
    Searches SHIP_DICTIONARY for ship_name and prints information about matching ship(s)
    """
    no_match = True
    for ship in SHIP_DICTIONARY:
        if ship_name.lower() in ship["SHIPNAME"].lower():
            no_match = False
            print(ship["SHIPNAME"])
    if no_match:
        print(f"No ship(s) found with search: {ship_name}")


def get_user_input() -> tuple:
    """
    gets a string from user, converts it into a list, checks if valid and returns the list.
    """
    user_input = input("Enter a command: ")
    command, *args = user_input.strip().split(" ")
    return command, args


FUNCTION_DICT = {
    "help": {
        "function": print_commands,
        "parameter": ""
    },
    "show_countries": {
        "function": print_all_countries_no_duplicates,
        "parameter": ""
    },
    "top_countries": {
        "function": print_top_countries_and_ship_count,
        "parameter": "<num_countries>"
    },
    "search_ship": {
        "function": search_ship,
        "parameter": "<name>"
    },
    "ships_by_types": {
        "function": ships_by_types,
        "parameter": ""
    },
    "quit": {
        "function": exit,
        "parameter": ""
    }
}


def main():
    print("Welcome to my Ships CLI! Enter 'help' to view available commands.")
    while True:
        command, args = get_user_input()
        try:
            FUNCTION_DICT[command.lower()]["function"](*args)
        except TypeError:
            print("Parameter not valid")
        except KeyError:
            print("Command not found")
        except Exception as e:
            print("Critical Error: ", e)
            exit(1)


if __name__ == "__main__":
    main()
