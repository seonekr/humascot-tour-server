# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import( 
    CategoryTourViewSet,               
    CategoryHotelViewSet,               
    CategoryRestaurantViewSet,               
    CategoryTicketViewSet,               
    CategoryPacketViewSet,               
    CategoryGuideViewSet,               
    SitemainViewSet,
    SitemainImageViewSet,
    TourViewSet,
    TourImageViewSet,
    HotelViewSet,
    HotelImageViewSet,
    RestaurantViewSet,
    RestaurantImageViewSet,
    TicketViewSet,
    TicketImageViewSet,
    PacketViewSet,
    PacketImageViewSet,
    GuideViewSet,
    GuideImageViewSet,
)

router = DefaultRouter()
#1
router.register(r'sitemain', SitemainViewSet)
router.register(r'sitemain-images', SitemainImageViewSet)
#2  
router.register(r'tour', TourViewSet)
router.register(r'tour-images', TourImageViewSet)
router.register(r'tour-Category', CategoryTourViewSet)
#3
router.register(r'hotel', HotelViewSet)
router.register(r'hotel-images', HotelImageViewSet)
router.register(r'hotel-Category', CategoryHotelViewSet)
#4
router.register(r'restaurant', RestaurantViewSet)
router.register(r'restaurant-images', RestaurantImageViewSet)
router.register(r'restaurant-Category', CategoryRestaurantViewSet)
#5
router.register(r'ticket', TicketViewSet)
router.register(r'ticket-images', TicketImageViewSet)
router.register(r'ticket-Category', CategoryTicketViewSet)
#6
router.register(r'packet', PacketViewSet)
router.register(r'packet-images', PacketImageViewSet)
router.register(r'packet-Category', CategoryPacketViewSet)
#7
router.register(r'guide', GuideViewSet)
router.register(r'guide-images', GuideImageViewSet)
router.register(r'guide-Category', CategoryGuideViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
