//we_can_pick.js

function addMoreFields() {
	var inputCount = document.getElementsByTagName('input').length;
	var addButton = document.getElementById('add-more');
	if (inputCount <= 10) {
		var input = document.createElement('input');
		input.name = "input" + inputCount;
		input.type = "text";
		input.required =true;
		var form = document.getElementById('we-can-pick-page-form');
		form.insertBefore(input, addButton);
	}
	else {
		alert("Please limit yourselves to 10 options, we can't make all of the decisions!");
	}
}