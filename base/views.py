import json
from django.http import  JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render


import requests
from rest_framework.views import APIView
from .models import Product
from .serializer import ProductSerializer

def fetch_data_from_db():
    url = 'http://localhost:4000/prods'
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    print(data)  

fetch_data_from_db()


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def tasks(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def index(req):
    return JsonResponse('hola!', safe=False)

