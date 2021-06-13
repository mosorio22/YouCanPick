//home.js

function addMoreFields() {
	if (document.getElementsByTagName('input').length <= 10) {
		var input = document.createElement('input');
		var form = document.getElementsByClassName('home-page-form')[0];
		form.insertBefore(input, form[0])
	}
	else {
		alert("Please limit yourselves to 10 options, we can't make all of the decisions!");
	}
}