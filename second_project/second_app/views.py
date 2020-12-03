from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(requests):
    return HttpResponse('<em>My Second App</em>')


def help_view(requests):
    a_dictionary = {'please_insert_me_here': 'Help Page'}
    return render(requests, 'second_app/help.html', context=a_dictionary)
