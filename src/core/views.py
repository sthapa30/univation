from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Car

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/car-list'
    }
    return Response(api_urls)

@api_view(['GET'])
def carlist(request):
    cars = Car.objects.all()
    serializer = PostSerializer(cars,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def carCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def carUpdate(request,pk):
    car = Car.objects.get(id=pk)
    serializer = PostSerializer(instance=car, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def carDelete(request,pk):
    car = Car.objects.get(id=pk)
    car.delete()
    return Response('Item deleted')
