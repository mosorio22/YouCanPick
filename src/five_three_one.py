#5-3-1 page
@app.route("/five_three_one", methods=['GET', 'POST'])
def five_three_one():
	request_data = list(request.form.values())
	if request.method == "POST":
		#first submit - give 5 initial options and cut it down to 3
		if len(request_data) == 5:
			print("1st submit")
			first_place = random.choice(request_data)
			request_data.remove(first_place)
			second_place = random.choice(request_data)
			request_data.remove(second_place)
			third_place = random.choice(request_data)
			request_data.remove(third_place)
			return render_template("five-three-one.html", second_run = True, first_place = first_place, second_place = second_place, third_place = third_place)
		#second submit - user can narrow it down to 1
		elif len(request_data) == 3:
			print("2nd visit")
			our_choice = request_data
			return render_template("five-three-one.html", last_run = True, our_choice = our_choice)
	#first visit on page - get initial form
	print("1st visit")
	return render_template("five-three-one.html", first_run = True)