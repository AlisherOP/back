from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework. permissions import IsAuthenticated, AllowAny
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    permission_classes=[AllowAny]


def index(request):
    item_list = Item.objects.all().order_by('-id')

    food_name = request.GET.get('food_name')
    if food_name != "" and food_name is not None:
        item_list = item_list.filter(item_name__icontains=food_name)

    paginator = Paginator(item_list, 3)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)
    context = {
        "item_list": item_list,
        "food_name": food_name,

    }
    return render(request, "food/index.html", context)
