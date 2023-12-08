from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world !")


def user_list(request):
    return render(request, "user_list.html")
    # return HttpResponse("User list")


