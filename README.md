# GitHub Repository Analyzer

The GitHub Repository Analyzer is a Python script that uses the GitHub API to fetch and analyze repositories for a given user. It lists the programming languages used across the fetched repositories, displaying which languages are most commonly used.

## Features

- Fetch repositories for any given GitHub username
- Count and list usage of programming languages across repositories
- Utilize GitHub API without needing personal access tokens for public data

## Getting Started

To run this script, you will need Python and the `requests` package installed on your system.

### Prerequisites

- Python
- `requests` package (install using `pip install requests`)

### Usage

Run the script with:

```bash
python github_repo_analyzer.py
```

Enter a valid GitHub username when prompted. The script will output a list of languages used by the provided GitHub user's repositories, along with the count for each language.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
