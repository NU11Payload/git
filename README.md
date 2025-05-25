# GitHub Repo Scrubber 🧹

A Python script for when you need a fresh start on GitHub. This tool helps you bulk delete your repositories when you've gone a bit fork-happy or need to clean up your GitHub profile.

## ⚠️ WARNING ⚠️
**THIS SCRIPT DELETES REPOSITORIES. THIS ACTION IS IRREVERSIBLE.**
- Make sure you have backups of anything important
- Double check your username is correct
- Consider downloading your repos before deletion
- The script will skip repositories named "readme" to prevent accidental deletion

## Setup 🛠️

1. Clone this repository
2. Create a `.env` file from `.env.example`:
   ```bash
   cp .env.example .env
   ```
3. Get a GitHub Personal Access Token:
   - Go to GitHub Settings > Developer Settings > Personal Access Tokens
   - Generate a new token with `delete_repo` scope
   - Copy the token to your `.env` file

4. Install dependencies:
   ```bash
   pip install python-dotenv requests
   ```

5. Edit the script to add your GitHub username:
   ```python
   USERNAME = "your_username_here"
   ```

## Usage 🚀

```bash
python delete.py
```

The script will:
1. List all your repositories
2. Show you how many it found
3. Begin deletion process
4. Skip any repository named "readme"
5. Report success/failure for each deletion

## Safety Features 🛡️
- Skips README repositories
- Requires explicit username configuration
- Uses environment variables for token security
- Shows preview of repos before deletion

## Requirements 📋
- Python 3.6+
- `requests` library
- `python-dotenv` library
- GitHub Personal Access Token with `delete_repo` scope 