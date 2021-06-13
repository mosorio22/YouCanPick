from flask import Flask, render_template, request
import random

app = Flask(__name__)

#home page
@app.route("/", methods=['GET', 'POST'])
def home():
	request_data = request.form
	if request.method == "POST":
		random_restaurant = random.choice(list(request_data.values()))
		return render_template("home.html", random_restaurant = random_restaurant)
	return render_template("home.html")

#about page
@app.route("/about")
def about():
	return render_template("about.html")

#5-3-1 page
@app.route("/five_three_one", methods=['GET', 'POST'])
def five_three_one():
	#return render_template("five-three-one.html")
	request_data = request.form
	if request.method == "POST":
		#first submit - get 3 random values
		if len(request_data) == 5:
			first_place = random.choice(list(request_data.values()))
			del request_data[first_place]
			second_place = random.choice(list(request_data.values()))
			del request_data[second_place]
			third_place = random.choice(list(request_data.values()))
			del request_data[third_place]
			return render_template("five-three-one.html", second_run = True, first_place = first_place, second_place = second_place, third_place = third_place)
		#second submit - get restaurant choice
		elif len(request_data) == 3:
			random_restaurant = random.choice(list(request_data.values()))
			return render_template("five-three-one.html", last_run = True, random_restaurant = random_restaurant)
	#first visit on page - get initial form
	return render_template("five-three-one.html", first_run = True)

if __name__ == "__main__":
	app.run()