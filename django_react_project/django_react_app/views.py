from django.shortcuts import render
from django.core import serializers
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django_react_app.models import Product
# Create your views here.


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


def prductsView(request):
    snippets = Product.objects.all()
    serializer = ProductsSerializer(snippets, many=True)
    products = str(JSONRenderer().render(serializer.data), 'utf-8')

    context = {
        'django_products': Product.objects.all(),
        'react_products': products
    }

    return render(request, 'products.html', context=context)
