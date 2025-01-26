from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


# class bookingview(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items, many=True)
#         return Response(serializer.data)  # return JSON


# class menuview(APIView):
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = menuSerializer(items, many=True)
#         return Response(serializer.data)  # return JSON

#     def post(self, request):
#         serializer = menuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
