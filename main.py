from flask import Flask, render_template, request
import random

app = Flask(__name__)


#home page
@app.route("/")
def home():
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