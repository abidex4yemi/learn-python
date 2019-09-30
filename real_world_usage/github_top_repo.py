import requests

api_url = "https://api.github.com/search/repositories"


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repo_with_most_stars(url, query="stars:>50000", sort="stars", order="asc"):
    response = requests.get(url, {"q": query, "sort": sort, "order": order})
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError("An error ocurred when fetching list of repo")
    else:
        repo = response.json()

    return repo["items"]


if __name__ == "__main__":
    query = create_query(languages=["Python", "Javscript", "Ruby"])

    result = repo_with_most_stars(api_url, query, sort="stars", order=" ")

    for repo in result:
        language = repo["language"]
        star = repo["stargazers_count"]
        name = repo["name"]

        print(f"-> {name} is a {language} repo with {star} stars.")
