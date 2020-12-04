from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User


# Create your views here.
def index(requests):
    return HttpResponse('<em>My Second App</em>')


def help_view(request):
    a_dictionary = {'please_insert_me_here': 'Please refer to /users page.'}
    return render(request, 'second_app/help.html', context=a_dictionary)


def user_view(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users': users_list}
    return render(request, 'users/index.html', context=user_dict)
