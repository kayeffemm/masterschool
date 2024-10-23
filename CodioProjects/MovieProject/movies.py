import movie_storage, statistics, random


def movie_stats():
    """
    Calls list_movies function to get all data and prints the average, median rating.
    Also identifies the worst and best movies and saves them to a list.
    Then parses both lists to print_list_of_tuple function to get a printable string.
    """
    movies = movie_storage.list_movies()
    rating_list = [float(movie["rating"]) for movie in movies]

    average_rating = sum(rating_list) / len(rating_list)
    median_rating = statistics.median(rating_list)

    best_rating = max(rating_list)
    worst_rating = min(rating_list)

    best_movies = [(movie["title"], movie["rating"]) for movie in movies if float(movie["rating"]) == best_rating]
    worst_movies = [(movie["title"], movie["rating"]) for movie in movies if float(movie["rating"]) == worst_rating]

    print(f"Average rating: {average_rating}")
    print(f"Median ratinig: {median_rating}")
    print(f"Best movie(s): {print_list_of_tuple(best_movies)}")
    print(f"Worst movie(s): {print_list_of_tuple(worst_movies)}")


def print_list_of_tuple(a_list: list) -> str:
    """
    Helper function to convert list of tuples into a string and returns it.
    """
    if len(a_list) > 1:
        string_to_print = ""
        for item in a_list:
            string_to_print += f"({item[0]}, {item[1]}) "
        return string_to_print
    else:
        return f"{a_list[0][0]}, {a_list[0][1]}"


def random_movie():
    """
    uses the random module to get a pseudo-random entry from the movies list and prints it.
    """
    movies = movie_storage.list_movies()
    random_movie_dictionary = random.choice(movies)
    title = random_movie_dictionary["title"]
    rating = random_movie_dictionary["rating"]
    print(f"You could watch this movie: {title}, it\'s rated {rating}")


def search_movie(search_term: str):
    """
    TODO write
    """
    pass


def main():
    #print(get_property_count(movie_storage.list_movies(), "rating"))
    random_movie()

if __name__ == "__main__":
    main()