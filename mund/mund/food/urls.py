from . import views
from django.urls import path

app_name= "food"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:product_id>/", views.detail, name="detail"),
    path("add", views.add, name="add"),
    path("delete/<int:id>", views.delete_product, name= "delete_product")
]