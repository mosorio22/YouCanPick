# YouCanPick

Description:
YouCanPick is a web app built using Flask meant to help indecisive people choose where to eat next. There are 2 features to YouCanPick. On the home page, criteria are used to search for restaurants using Yelp's api. There is also the WeCanPick page that randomly chooses between user input to help users decide between different restaurant options.

Usage:
To start the web app locally, just clone the repo and get packages from requirements.txt. Then run main.py from your working directory or your virtual environment.
NOTE: To use this web app's home page search feature, a Yelp api key is needed.
**Do not commit the secret api key to this project**

### Yelp Fusion API Key Storage
1. Create a directory named `resources` within the root `YouCanPick` project directory.
2. Create a file in the `resources` directory named `api.json`.
3. Copy the below JSON snippet into `api.json` and insert your client_id and api_key into the JSON.
```
{
  "client_id": "",
  "api_key": ""
}
```
4. **Do not commit `api.json` to the Git repo. This file should be stored locally for security purposes.**

#### TODO
Make fully responsive

License:
MIT
