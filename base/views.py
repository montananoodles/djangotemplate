from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



from base.models import Book
from base.serializer import BookSerializer

# Create your views here.
def index(req):
    return JsonResponse('hola!', safe=False)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['emailllll'] = user.email
        token['username'] = user.username
        token['waga'] = "baga"

        # For testing purposes
        print("testtttttttttttt")

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(req):
    return Response("im protected")

@api_view(['GET', 'DELETE', 'PUT', 'POST'])
def books(req, id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_book=Book.objects.get(id=id)
                return Response (BookSerializer(temp_book,many=False).data)
            except Book.DoesNotExist:
                return Response ("not found")
        all_Books=BookSerializer(Book.objects.all(),many=True).data
        return Response (all_Books)
    
    if req.method =='POST':
        book_serializer = BookSerializer(data=req.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response ("post...")
        else:
            return Response (book_serializer.errors)
        
    if req.method =='DELETE':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_book.delete()
        return Response ("del...")
    
    if req.method =='PUT':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")
       
        ser = BookSerializer(data=req.data)
        old_task = Book.objects.get(id=id)
        res = ser.update(old_task, req.data)
        return Response(res)
