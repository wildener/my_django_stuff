from django.conf.urls import url
from second_app import views

urlpatterns = [
    url(r'^$', views.user_view, name='users')
]
