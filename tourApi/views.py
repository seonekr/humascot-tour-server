# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status, generics, filters
from django.http import Http404
from .models import Tour, Hotel, Restaurant, Packet, Guide

from .serializers import (
    TourSerializer,
    TourCreateSerializer,
    HotelSerializer,
    HotelCreateSerializer,
    RestaurantSerializer,
    RestaurantCreateSerializer,
    PacketSerializer, PacketCreateSerializer,
    GuideSerializer, GuideCreateSerializer
)


# ====================================================================================================
# Tour management's by oudone
class TourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class TourRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Tour not found"})


class TourCreateAPIView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class TourUpdateAPIView(generics.UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Tour not found"})


class TourDestroyAPIView(generics.DestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Tour not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# ====================================================================================================


# Hotel management's by oudone
class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class HotelRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Hotel not found"})


class HotelCreateAPIView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class HotelUpdateAPIView(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Hotel not found"})


class HotelDestroyAPIView(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Hotel not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    

# Restaurant management's by oudone
class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class RestaurantRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Restaurant not found"})


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class RestaurantUpdateAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Restaurant not found"})


class RestaurantDestroyAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Restaurant not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)


# Packet management's by oudone
class PacketListAPIView(generics.ListAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class PacketRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Packet not found"})


class PacketCreateAPIView(generics.CreateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class PacketUpdateAPIView(generics.UpdateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Packet not found"})


class PacketDestroyAPIView(generics.DestroyAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Packet not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    


# Guide management's by oudone
class GuideListAPIView(generics.ListAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # Specify fields you want to search


class GuideRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Guide not found"})


class GuideCreateAPIView(generics.CreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class GuideUpdateAPIView(generics.UpdateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideCreateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        # Custom logic before saving if needed
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Guide not found"})


class GuideDestroyAPIView(generics.DestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Guide not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    
    
    
    
    