from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import demo
from .serializer import demoSerializer
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
 
# Create your views here.
@api_view(['POST'])
def add_items(request):
    item = demoSerializer(data=request.data)
 
    # validating for already existing data
    if demo.objects.filter(**request.data).exists():
        raise demoSerializer.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = demo.objects.filter(**request.query_params.dict())
    else:
        items = demo.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = demoSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_items(request, id):
    item = demo.objects.get(id=id)
    data = demoSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)