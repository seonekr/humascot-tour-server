# serializers.py
from rest_framework import serializers
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

#1
class SitemainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagebannerModel
        fields = '__all__'

class SitemainSerializer(serializers.ModelSerializer):
    banners = serializers.SerializerMethodField()

    def get_banners(self, obj):
        banners = ImagebannerModel.objects.filter(banner=obj)
        serializer = SitemainBannerSerializer(banners, many=True)
        return [i['image'] for i in serializer.data]
    
    class Meta:
        model = Sitemain
        fields = ["id", "name", "banners", "logo", "created_at"]
        
#2
class CategoryTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModelTour
        fields = '__all__'
            
class ImageTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTourModel
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageTourModel.objects.filter(tour=obj)
        serializer = ImageTourSerializer(images, many=True)
        return [i['image'] for i in serializer.data]

    class Meta:
        model = Tour
        fields = ["id", "category", "name", "image", "images", "description", "price", "address"]

# create tour by oudone
class TourCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)
    class Meta:
        model = Tour
        fields = ["id", "category", "name", "image", "images", "description", "price", "address"]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        
        tour = Tour.objects.create(**validated_data)
        
        for image_file in images_data:
            image = ImageTourModel.objects.create(tour=tour, image=image_file)
        
        return tour
    
    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])
        
        # Update Tour fields
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        if images_data:
            # Clear existing images if any
            ImageTourModel.objects.filter(tour=instance).delete()
            # Add new images
            for image_file in images_data:
                ImageTourModel.objects.create(tour=instance, image=image_file)

        return instance

#3
class CategoryHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModelHotel
        fields = '__all__'
        
class ImageHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHotelModel
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    category = CategoryHotelSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageHotelModel.objects.filter(hotel=obj)
        serializer = ImageHotelSerializer(images, many=True)
        return [i['image'] for i in serializer.data]
    
    class Meta:
        model = Hotel
        fields = ["id", "category", "name", "image", "images", "description", "price", "address"]

#4
class CategoryRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModelRestaurant
        fields = '__all__'

class ImageRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRestaurantModel
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    category = CategoryRestaurantSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageRestaurantModel.objects.filter(restaurant=obj)
        serializer = ImageRestaurantSerializer(images, many=True)
        return [i['image'] for i in serializer.data]
    
    class Meta:
        model = Restaurant
        fields = ["id", "category", "name", "image", "description", "address", "images"]
        
#5
class CategoryTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModelTicket
        fields = '__all__'

class ImageTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTicketModel
        fields = '__all__'
        
class TicketSerializer(serializers.ModelSerializer):
    category = CategoryTicketSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageTicketModel.objects.filter(ticket=obj)
        serializer = ImageTicketSerializer(images, many=True)
        return [i['image'] for i in serializer.data]
    class Meta:
        model = Ticket
        fields = ["id", "category","name","image","images","description","address","price","brand","carnumber"]
#6
class CategoryPacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModelPacket
        fields = '__all__'

class ImagePacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePacketModel
        fields = '__all__'
        
class PacketSerializer(serializers.ModelSerializer):
    category = CategoryPacketSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImagePacketModel.objects.filter(packet=obj)
        serializer = ImagePacketSerializer(images, many=True)
        return [i['image'] for i in serializer.data]
    
    class Meta:
        model = Packet
        fields = ["id","category","name","image","images","description","address","price"]

#7
class CategoryGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModelGuide
        fields = '__all__'

class ImageGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGuideModel
        fields = '__all__'
        
class GuideSerializer(serializers.ModelSerializer):
    category = CategoryGuideSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ImageGuideModel.objects.filter(guide=obj)
        serializer = ImageGuideSerializer(images, many=True)
        return [i['image'] for i in serializer.data]
    
    class Meta:
        model = Guide
        fields = ["id", "category", "name", "image", "images", "description", "address"]
