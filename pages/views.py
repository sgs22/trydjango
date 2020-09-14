from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>") #string of html code
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "this is about us",
		"this_is_true": True,
		"my_number": 123,
		"my_list": [1313,4321,321,"Abc"]
		
	}
	return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})