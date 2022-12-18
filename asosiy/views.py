from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
# Create your views here.

class K_BoblarViewSet(ModelViewSet):
    queryset = Konstitsiya_Bob.objects.all()
    serializer_class = K_BobSerializer

# class K_BoblarAPIView(APIView):
#     def get(self,request):
#         boblar = Konstitsiya_Bob.objects.all()
#         serializer = K_BobSerializer(boblar, many=True)
#         natija = {
#             "Succeess": serializer.data
#         }
#         return Response(natija)