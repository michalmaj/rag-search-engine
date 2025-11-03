from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies
import string


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for movie in movies:
        preprocessed_query = preprocess_text(query)
        preprocessed_title = preprocess_text(movie["title"])
        if any(q in t for q in preprocessed_query for t in preprocessed_title):
            results.append(movie)
            if len(results) >= limit:
                break
    return results


def preprocess_text(text: str) -> str:
    # Convert to lower
    text = text.lower()

    # Remove punctuation
    table = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(table)

    # Split into tokens
    tokens = [t for t in text.split() if t]

    return tokens
