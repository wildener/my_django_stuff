from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    e_mail = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
