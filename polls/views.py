from django.http import HttpResponse


def index(request):
	print "HOLA MUNDO"
    return HttpResponse("Hello, world. You're at the polls index.")
	