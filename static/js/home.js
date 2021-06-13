//home.js

function addMoreFields() {
	var inputCount = document.getElementsByTagName('input').length;
	if (inputCount <= 10) {
		var input = document.createElement('input');
		input.name = "input" + inputCount;
		input.type = "text";
		input.required =true;
		var form = document.getElementsByClassName('home-page-form')[0];
		form.insertBefore(input, form[0])
	}
	else {
		alert("Please limit yourselves to 10 options, we can't make all of the decisions!");
	}
}