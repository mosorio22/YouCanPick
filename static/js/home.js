//home.js

function addMoreFields() {
	var inputCount = document.getElementsByTagName('input').length;
	var addButton = document.getElementById('add-more');
	if (inputCount <= 10) {
		var input = document.createElement('input');
		input.name = "input" + inputCount;
		input.type = "text";
		input.required =true;
		var form = document.getElementsByClassName('home-page-form')[0];
		form.insertBefore(input, addButton);
	}
	else {
		alert("Please limit yourselves to 10 options, we can't make all of the decisions!");
	}
}