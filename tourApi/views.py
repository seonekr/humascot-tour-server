# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from .models import ( 
    CategoryModelTour,
    CategoryModelHotel,
    CategoryModelRestaurant,
    CategoryModelTicket,
    CategoryModelPacket,
    CategoryModelGuide,
    Sitemain,
    ImagebannerModel,
    Tour,
    ImageTourModel,
    Hotel,
    ImageHotelModel,
    Restaurant,
    ImageRestaurantModel,
    Ticket,
    ImageTicketModel,
    Packet,
    ImagePacketModel,
    Guide,
    ImageGuideModel,
)

from .serializers import ( 
    CategoryTourSerializer,
    CategoryHotelSerializer,
    CategoryRestaurantSerializer,
    CategoryTicketSerializer,
    CategoryPacketSerializer,
    CategoryGuideSerializer,
    SitemainSerializer,
    SitemainBannerSerializer,
    TourSerializer,
    ImageTourSerializer,
    HotelSerializer,
    ImageHotelSerializer,
    RestaurantSerializer, 
    ImageRestaurantSerializer,
    TicketSerializer,
    ImageTicketSerializer,
    PacketSerializer,
    ImagePacketSerializer,
    GuideSerializer,
    ImageGuideSerializer,
)


class CategoryHotelViewSet(viewsets.ModelViewSet):
    queryset = CategoryModelHotel.objects.all()
    serializer_class = CategoryHotelSerializer
class CategoryRestaurantViewSet(viewsets.ModelViewSet):
    queryset = CategoryModelRestaurant.objects.all()
    serializer_class = CategoryRestaurantSerializer
class CategoryTicketViewSet(viewsets.ModelViewSet):
    queryset = CategoryModelTicket.objects.all()
    serializer_class = CategoryTicketSerializer
class CategoryPacketViewSet(viewsets.ModelViewSet):
    queryset = CategoryModelPacket.objects.all()
    serializer_class = CategoryPacketSerializer
class CategoryGuideViewSet(viewsets.ModelViewSet):
    queryset = CategoryModelGuide.objects.all()
    serializer_class = CategoryGuideSerializer


#main page API 1
class SitemainViewSet(viewsets.ModelViewSet):
    queryset = Sitemain.objects.all()
    serializer_class = SitemainSerializer

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        sitemain = self.get_object()
        serializer = SitemainBannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sitemain=sitemain)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SitemainImageViewSet(viewsets.ModelViewSet):
    queryset = ImagebannerModel.objects.all()
    serializer_class = SitemainBannerSerializer

#Tour API 2
class CategoryTourViewSet(viewsets.ModelViewSet):
    queryset = CategoryModelTour.objects.all()
    serializer_class = CategoryTourSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        tour = self.get_object()
        serializer = ImageTourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tour=tour)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TourImageViewSet(viewsets.ModelViewSet):
    queryset = ImageTourModel.objects.all()
    serializer_class = ImageTourSerializer

#Hotel API 3
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        hotel = self.get_object()
        serializer = ImageHotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hotel=hotel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = ImageHotelModel.objects.all()
    serializer_class = ImageHotelSerializer

#Restaurant API 4
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        restaurant = self.get_object()
        serializer = ImageRestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=restaurant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantImageViewSet(viewsets.ModelViewSet):
    queryset = ImageRestaurantModel.objects.all()
    serializer_class = ImageRestaurantSerializer

#Packet API 5
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        ticket = self.get_object()
        serializer = ImageTicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ticket=ticket)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketImageViewSet(viewsets.ModelViewSet):
    queryset = ImageTicketModel.objects.all()
    serializer_class = ImageTicketSerializer 


#Packet API 6
class PacketViewSet(viewsets.ModelViewSet):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        packet = self.get_object()
        serializer = ImagePacketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(packet=packet)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PacketImageViewSet(viewsets.ModelViewSet):
    queryset = ImagePacketModel.objects.all()
    serializer_class = ImagePacketSerializer 

#Guide API 7
class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        guide = self.get_object()
        serializer = ImageGuideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(guide=guide)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuideImageViewSet(viewsets.ModelViewSet):
    queryset = ImageGuideModel.objects.all()
    serializer_class = ImageGuideSerializer 
    

