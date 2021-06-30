# YouCanPick

Description:
YouCanPick is a web app built using Flask meant to help indecisive people choose where to eat next. There are 2 features to YouCanPick. On the home page, criteria are used to search for restaurants using Yelp's api. There is also the WeCanPick page that randomly chooses between user input to help users decide between different restaurant options.

License:
MIT

Usage:
To start the web app locally, just clone the repo and get packages from requirements.txt. Then run main.py from your working directory or your virtual environment.
NOTE: To use this web app's home page search feature, a Yelp api key is needed.
**Do not commit the secret api key to this project**

### Yelp Fusion API Key
#### Development Environment Setup
1. Obtain a Yelp Fusion API key: https://www.yelp.com/developers/documentation/v3/authentication
2. Create an empty `.env` file in the project root directory.
3. Copy the following snippet into the `.env` file, substituting `INSERT_API_KEY` with your Yelp Fusion API key.
```
YELP_FUSION_API_KEY=INSERT_API_KEY
```
**Note:** Do not commit the `.env` file to Git.
