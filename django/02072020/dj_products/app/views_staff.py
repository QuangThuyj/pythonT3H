from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from . import db
from .models import Product
from .forms import ProductForm


def listProduct(request):
    keyword = request.GET.get('keyword', '')
    categoryId = request.GET.get('categoryId', '')
    freeShip = request.GET.get("freeShip", '') == '1'
    categories = db.getCategories()
    products = db.getProducts(keyword, categoryId, freeShip)
    return render(request, 'staff/product_list.html',
                  {
                      'products': products,
                      'keyword': keyword,
                      'freeShip': freeShip,
                      'categoryId': int(categoryId or "0"),
                      'categories': categories
                  })


def addProduct(request):
    backURL = request.GET.get('back_url', reverse_lazy('listProduct'))
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(backURL)

    return render(request, 'staff/product.html', {'form': form, 'backURL': backURL})


def editProduct(request, id):
    backURL = request.GET.get('back_url', reverse_lazy('listProduct'))
    product = db.findProductById(id)
    form = ProductForm(instance=product)
    form.initial['id'] = id

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(backURL)

    return render(request, 'staff/product.html', {'form': form, 'backURL': backURL})


def deleteProduct(request, id):
    backURL = request.GET.get('back_url', reverse_lazy('listProduct'))
    product = get_object_or_404(Product, pk=id)
    if product:
        product.delete()
    return redirect(backURL)
