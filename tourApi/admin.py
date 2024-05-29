from django.contrib import admin
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

@admin.register(CategoryModelTour)
class Category1Admin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("id", "name")

    search_fields = ("name",)
    
@admin.register(CategoryModelHotel)
class Category2Admin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("id", "name")

    search_fields = ("name",)
    
@admin.register(CategoryModelRestaurant)
class Category3Admin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("id", "name")

    search_fields = ("name",)
    
@admin.register(CategoryModelTicket)
class Category4Admin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("id", "name")

    search_fields = ("name",)
    
@admin.register(CategoryModelPacket)
class Category5Admin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("id", "name")

    search_fields = ("name",)
    
@admin.register(CategoryModelGuide)
class Category6Admin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("id", "name")

    search_fields = ("name",)
    
    
    
@admin.register(Sitemain)
class SitemainAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name", "logo", "created_at")

    search_fields = ("name",)
    
@admin.register(ImagebannerModel)
class ImagebannerModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("banner", "image")

    search_fields = ("banner",)

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name", "image", "price", "address", "description")

    search_fields = ("name",)
    
@admin.register(ImageTourModel)
class ImageTourModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("tour", "image")

    search_fields = ("tour",)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name", "image", "address", "price","description")

    search_fields = ("name",)
    
@admin.register(ImageHotelModel)
class ImageHotelModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("hotel", "image")

    search_fields = ("hotel",)
    
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name", "image", "address","description")

    search_fields = ("name",)
    
@admin.register(ImageRestaurantModel)
class ImageRestaurantModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("restaurant", "image")

    search_fields = ("restaurant",)
    

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name", "image", "category", "price", "address", "description", "brand", "carnumber")

    search_fields = ("name",)
    
@admin.register(ImageTicketModel)
class ImageTicketModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("ticket", "image")

    search_fields = ("ticket",)
    

@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name","image","price","address", "description")

    search_fields = ("name",)
    
@admin.register(ImagePacketModel)
class ImagePacketModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("packet", "image")

    search_fields = ("packet",)
    
    
@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("name", "image", "address", "description")

    search_fields = ("name",)
    
@admin.register(ImageGuideModel)
class ImageGuideModelAdmin(admin.ModelAdmin):

    """Board Admin Definition"""

    list_display = ("guide", "image")

    search_fields = ("guide",)