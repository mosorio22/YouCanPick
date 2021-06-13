from flask import Flask, render_template, request
import random

app = Flask(__name__)

#home page
@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		request_data = list(request.form.values())
		print(request_data)
		random_restaurant = random.choice(request_data)
		return render_template("home.html", random_restaurant = random_restaurant)
	return render_template("home.html")

#about page
@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run()