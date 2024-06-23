movies = {
    "movie1": {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "genre": ["Drama", "Crime"]
    },
    "movie2": {
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "genre": ["Crime", "Drama"]
    },
    "movie3": {
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "genre": ["Action", "Crime", "Drama"]
    },
    "movie4": {
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "genre": ["Crime", "Drama"]
    },
    "movie5": {
        "title": "The Lord of the Rings: The Return of the King",
        "director": "Peter Jackson",
        "genre": ["Action", "Adventure", "Drama"]
    },
    "movie6": {
        "title": "Forrest Gump",
        "director": "Robert Zemeckis",
        "genre": ["Drama", "Romance"]
    },
    "movie7": {
        "title": "Inception",
        "director": "Christopher Nolan",
        "genre": ["Action", "Adventure", "Sci-Fi"]
    },
    "movie8": {
        "title": "Fight Club",
        "director": "David Fincher",
        "genre": ["Drama"]
    },
    "movie9": {
        "title": "The Matrix",
        "director": "Lana Wachowski, Lilly Wachowski",
        "genre": ["Action", "Sci-Fi"]
    },
    "movie10": {
        "title": "Goodfellas",
        "director": "Martin Scorsese",
        "genre": ["Biography", "Crime", "Drama"]
    },
    "movie11": {
        "title": "The Silence of the Lambs",
        "director": "Jonathan Demme",
        "genre": ["Crime", "Drama", "Thriller"]
    },
    "movie12": {
        "title": "The Usual Suspects",
        "director": "Bryan Singer",
        "genre": ["Crime", "Drama", "Mystery"]
    },
    "movie13": {
        "title": "Saving Private Ryan",
        "director": "Steven Spielberg",
        "genre": ["Drama", "War"]
    },
    "movie14": {
        "title": "Schindler's List",
        "director": "Steven Spielberg",
        "genre": ["Biography", "Drama", "History"]
    },
    "movie15": {
        "title": "The Green Mile",
        "director": "Frank Darabont",
        "genre": ["Crime", "Drama", "Fantasy"]
    }
}

# Sample user data (assuming user rated movie8)
user = {
    "rated_movies": ["movie8"],
    "preferred_genres": ["Drama"]  # Can be populated if user specifies preferences
}

# Define a function to calculate genre similarity (simple overlap here)
def genre_similarity(movie1, movie2):
    return len(set(movie1["genre"]) & set(movie2["genre"]))

# Recommend similar movies for the user
rated_movie = user["rated_movies"][0]
similar_movies = sorted([(movie_id, genre_similarity(movies[rated_movie], movies[movie_id])) for movie_id in movies if movie_id not in user["rated_movies"]], key=lambda x: x[1], reverse=True)[:4]  # Get top 4 most similar movies

for movie_id, similarity in similar_movies:
    print(f"Recommend {movies[movie_id]['title']} (genre similarity: {similarity})")
