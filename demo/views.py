from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import demo
from .serializer import demoSerializer
 
# Create your views here.
@api_view(['GET'])
def getDemo(request):
    demodetails = demo.objects.all()
    serializer = demoSerializer(demodetails, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postDemo(request):
    serializer = demoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
