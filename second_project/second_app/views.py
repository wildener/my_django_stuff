from django.shortcuts import render
# from django.http import HttpResponse
# from second_app.models import User
from second_app.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')


def user_view(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request, 'second_app/users.html', {'form': form})
