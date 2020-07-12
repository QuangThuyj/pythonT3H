from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Product
from . import db
from django.urls import reverse_lazy


def index(request):
    keyword = request.GET.get('keyword', '')
    categoryId = request.GET.get('categoryId', '')
    categories = db.getCategories()
    products = db.getProducts(keyword, categoryId, False)
    return render(request, 'user/index.html', {
        'products': products,
        'keyword': keyword,
        'categoryId': int(categoryId or "0"),
        'categories': categories
    })


def productDetail(request, id):
    backURL = request.GET.get('back_url', reverse_lazy('home'))
    product = get_object_or_404(Product, pk=id)
    return render(request, 'user/product.html', {'product': product, 'backURL': backURL})


def findItem(cart, productId):
    for item in cart:
        if item['id'] == productId:
            return item


def getTotal(cart):
    return int(sum([x['qty'] * x['unitPrice'] for x in cart]))


def addToCart(request):
    productId = int(request.GET['productId'])
    qty = int(request.GET['qty'])

    product = get_object_or_404(Product, pk=productId)

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']
    item = findItem(cart, productId)

    if item:
        item['qty'] += qty
        item['total'] = int(item['qty'] * item['unitPrice'])
    else:
        cart.append({
            'id': productId,
            'name': product.name,
            'unitPrice': product.unitPrice,
            'qty': qty,
            'total': int(qty * product.unitPrice)
        })

    request.session['cartTotal'] = getTotal(cart)

    return redirect(request.GET.get('back_url', reverse_lazy('home')))


def viewCart(request):
    return render(request, 'user/view_cart.html')


def updateCartItem(request):
    productId = int(request.GET['productId'])
    qty = int(request.GET['qty'])

    if 'cart' in request.session:
        cart = request.session['cart']
        item = findItem(cart, productId)
        if item:
            item['qty'] = qty
            item['total'] = int(qty * item['unitPrice'])

        request.session['cart'] = cart
        request.session['cartTotal'] = getTotal(cart)

    return HttpResponse("OK")


def deleteCartItem(request):
    productId = int(request.GET['productId'])

    if 'cart' in request.session:
        cart = request.session['cart']
        item = findItem(cart, productId)

        if item:
            cart.remove(item)

        if len(cart) > 0:
            request.session['cart'] = cart
            request.session['cartTotal'] = getTotal(cart)
        else:
            del request.session['cart']
            del request.session['cartTotal']

    return HttpResponse("OK")


def clearCart(request):
    del request.session['cartTotal']
    del request.session['cart']
    return redirect('home')


def paymentInfo(request):
    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            fields = ('fullname', 'mobile', 'email', 'address')
            paymentInfo = {field: form.cleaned_data[field] for field in fields}
            request.session['paymentInfo'] = paymentInfo
            return redirect('confirmPayment')

    return render(request, 'user/payment_info.html', {'form': form})


def confirmPayment(request):
    return render(request, 'user/confirm_payment.html')


def thankYou(request):
    del request.session['cart']
    del request.session['cartTotal']
    del request.session['paymentInfo']
    return render(request, 'user/thankyou.html')


def contact(request):
    return render(request, 'user/contact.html')
