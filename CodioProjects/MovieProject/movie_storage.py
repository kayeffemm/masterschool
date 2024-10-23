import json

def list_movies() -> list:
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open("movie_database.json", "r") as file_reader:
            movies = json.load(file_reader)
    except FileNotFoundError as e:
        print(f"{e}\nInitializing empty list now...")
        movies = []
        #TODO ADD USER INPUT FUNCTION WHICH CALLS add_movie()
    return movies


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    #maybe check if data is NONE
    movies.append({
        "title": title,
        "year": year,
        "rating": rating
    })

    with open("movie_database.json", "w") as file_writer:
        json.dump(movies, file_writer, indent=4)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    del movies[next(i for i, movie in enumerate(movies) if movie["title"] == title)]

    with open("movie_database.json", "w") as file_writer:
        json.dump(movies, file_writer, indent = 4)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    index_of_dictionary_to_update = next(i for i, movie in enumerate(movies) if movie["title"] == title)
    movies[index_of_dictionary_to_update]["rating"] = rating

    with open("movie_database.json", "w") as file_writer:
        json.dump(movies, file_writer, indent = 4)


#add_movie("kek6", "2612", "9")
#delete_movie("kek")
#update_movie("kek", "5")