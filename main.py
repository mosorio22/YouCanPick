from flask import Flask, render_template, request
import random
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import src
from you_can_pick import you_can_pick
app = Flask(__name__)


#home page
@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		request_data = request.form
		random_restaurant = you_can_pick(request_data)
		# invalid zip code block
		if random_restaurant == "invalid":
			return render_template("home.html", invalid = random_restaurant)
		else:
			return render_template("home.html", random_restaurant =  random_restaurant)
	return render_template("home.html")

#we can pick page
@app.route("/we_can_pick", methods=['GET', 'POST'])
def we_can_pick():
	if request.method == "POST":
		request_data = list(request.form.values())
		random_restaurant = random.choice(request_data)
		return render_template("we_can_pick.html", random_restaurant = random_restaurant)
	return render_template("we_can_pick.html")

#about page
@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()