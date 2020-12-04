import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django

django.setup()

import random
from second_app.models import User
from faker import Faker


fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, e_mail=fake_email)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(150)
    print('populating complete!')
