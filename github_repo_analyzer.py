import requests
from collections import Counter

# The main function
def main():
    username = input("Enter the GitHub username: ")
    
    # Fetch the repositories for the given user
    repos = fetch_repositories(username)
    
    # Analyze and display the results
    if repos:
        language_count = analyze_repositories(repos)
        print(f"Most commonly used languages by {username}:")
        for language, count in language_count.items():
            print(f"{language}: {count} repo(s)")
    else:
        print(f"No repositories found for user {username}")

# Fetch repositories for a given GitHub user
def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json() # Return the list of repositories
    else:
        print(f"Failed to fetch repositories for user {username}")
        return None

# Analyze the repositories to count the usage of each programming language
def analyze_repositories(repos):
    languages = [repo['language'] for repo in repos if repo['language']]
    return Counter(languages) # Count the occurrence of each language

# Entry point of the script
if __name__ == "__main__":
    main()