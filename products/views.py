from django.shortcuts import redirect,reverse,render,get_object_or_404
from .models import Product
from django.db.models import Q 
from django.contrib import messages


# Create your views here.

def all_products(request):
    """view to show all products, including sorting and search queries """

    products = Product.objects.all()

    if request.GET :
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"You did not enter any search criterial")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    context = {
        'products':products,
        'search_term':query,
    }
    return render(request , 'products/products.html',context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)