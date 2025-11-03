from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    context={
        "products": products,
    }
    return render(request,"food/index.html", context)

def detail(request,product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "food/detail.html", context)


def add(request):
    form= ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-form.html", {"form": form})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method=="POST":
        product.delete()
        return redirect("food:index")
    return render(request, "food/delete-product.html",{"product":product})
