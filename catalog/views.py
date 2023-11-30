from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list' : product_list
    }
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name,phone,message)

    return render(request, 'contacts.html')


def product(request, id):

    product = Product.objects.get(id=id)


    context = {
        'object' : product
    }


    return render(request, 'product.html', context)

