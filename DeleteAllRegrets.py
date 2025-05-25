import requests
from dotenv import load_dotenv
import os
#The noew to github scrub sponge for when you discover the start button, but it is far to late, you forked those repos, worry not!
# Use this script , to delete all your repos, and start fresh. So your senior developer doesn't leave you passive aggressive comments on your pull requests.
load_dotenv()
# Replace with your GitHub username and personal access token in the .env file, rename .env.example to .env 

USERNAME ="" #your username is not really a secret, but is REQUIRED for the script to work, so fill this out please. 
TOKEN = os.getenv("TOKEN")

# A way to rawdog the api in python, it works. On my machine at least(tm)
repos_url = f"https://api.github.com/user/repos"
headers = {"Authorization": f"token {TOKEN}"}


params = {"type": "owner", "per_page": 100, "sort":"updated", "direction": "desc"}  # Adjust per_page if needed
response = requests.get(repos_url, headers=headers, params=params)

print(f"going to fetch from {USERNAME}...")
def all_repos():
    all_repo = []
    page = 1 

    while True:
        params["page"] = page
        response = requests.get(repos_url, headers=headers, params=params) 
        page_repos = response.json()
        if not page_repos:
            break
        if response.status_code == 200:
            print(f"Fetching page {page}...")
            all_repo.extend(page_repos)
            page += 1
        else:
            print(f"Failed to fetch repositories. Status code: {response.status_code}")
            break
    return all_repo

repos = all_repos()
print(f"Found {len(repos)} repositories to delete.")
for repo in repos:
    print(f"- {repo['name']}: {repo['html_url']}")

if response.status_code == 200:
    repos = response.json()
    print(f"Found {len(repos)} repositories to delete.")
    
    for repo in repos:

        repo_name = repo["name"]
        delete_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
        delete_response = requests.delete(delete_url, headers=headers)
        if repo_name.startswith() or repo_name.lower() == "readme":
            print(f"Skipping repository: {repo_name} ya may wanna keep that one")
            continue
        if delete_response.status_code == 204:
            print(f"Deleted repository: {repo_name}")
        else:
            print(f"Failed to delete repository: {repo_name}. Status code: {delete_response.status_code}")
else:
    print(f"Failed to fetch repositories. Status code: {response.status_code}")

        
        # Delete the repository

