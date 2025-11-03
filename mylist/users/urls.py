from . import views
from django.urls import path


app_name = "users"
urlpatterns = [
    # food
    path("", views.profilepage, name='index'),
]
