from django.db import models

# Create your models here.


class CategoryModelHotel(models.Model):
    class Meta:
        db_table = "categoryHotel"
        verbose_name_plural = "3.3.3 Category Hotel Type"

    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return str(self.name)
class CategoryModelRestaurant(models.Model):
    class Meta:
        db_table = "categoryRestaurant"
        verbose_name_plural = "4.4.4 Category Restaurant Type"

    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return str(self.name)
class CategoryModelTicket(models.Model):
    class Meta:
        db_table = "categoryTicket"
        verbose_name_plural = "5.5.5 Category Ticket Type"

    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return str(self.name)
class CategoryModelPacket(models.Model):
    class Meta:
        db_table = "categoryPacket"
        verbose_name_plural = "6.6.6 Category Packet Type"

    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return str(self.name)
class CategoryModelGuide(models.Model):
    class Meta:
        db_table = "categoryGuide"
        verbose_name_plural = "7.7.7 Category Guide Type"

    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return str(self.name)


#1
class Sitemain(models.Model):
    class Meta:
        db_table = "site"
        verbose_name_plural = "1. Site main" 
    
    name = models.CharField(max_length=100, default="name")
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
class ImagebannerModel(models.Model):
    class Meta:
        db_table = "ImageBannerModel"
        verbose_name_plural = "1.1. image banner list"

    banner = models.ForeignKey(Sitemain, on_delete=models.CASCADE, verbose_name="Sitemain")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.banner.name}"

#2
class CategoryModelTour(models.Model):
    class Meta:
        db_table = "categoryTour"
        verbose_name_plural = "2.2.2 Category Tour Type"

    name = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return str(self.name)

class Tour(models.Model):
    class Meta:
        db_table = "tour"
        verbose_name_plural = "2. Tour" 

    category = models.ForeignKey(CategoryModelTour, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100, default="name")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0, verbose_name="price")
    address = models.TextField()
    
    def __str__(self):
        return str(self.name)
    
class ImageTourModel(models.Model):
    class Meta:
        db_table = "ImageTourModel"
        verbose_name_plural = "2.2. image tour list"

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Tour")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.tour.name}"
    
#3
class Hotel(models.Model):
    class Meta:
        db_table = "hotel"
        verbose_name_plural = "3. Hotel" 
        
    category = models.ForeignKey(CategoryModelHotel, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100, default="name")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0, verbose_name="price")
    address = models.TextField()

    def __str__(self):
        return str(self.name)

class ImageHotelModel(models.Model):
    class Meta:
        db_table = "ImageHotelModel"
        verbose_name_plural = "3.3. image hotel list"

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Hotel")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.hotel.name}"

#4  
class Restaurant(models.Model):
    class Meta:
        db_table = "restaurant"
        verbose_name_plural = "4. Restaurant" 
    category = models.ForeignKey(CategoryModelRestaurant, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100, default="name")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField()
    address = models.TextField()

    def __str__(self):
        return str(self.name)

class ImageRestaurantModel(models.Model):
    class Meta:
        db_table = "ImageRestaurantModel"
        verbose_name_plural = "4.4. image restaurant list"

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.restaurant.name}"

#5
class Ticket(models.Model):
    class Meta:
        db_table = "Ticket"
        verbose_name_plural = "5. ticket" 
        
    category = models.ForeignKey(CategoryModelTicket, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100, default="name")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField()
    address = models.TextField()
    price = models.PositiveIntegerField(default=0, verbose_name="price")
    brand = models.TextField(null=True, blank=True)
    carnumber = models.PositiveIntegerField(default=0, verbose_name="carnumber", null=True, blank=True)

    def __str__(self):
        return str(self.name)    

class ImageTicketModel(models.Model):
    class Meta:
        db_table = "ImageTicketModel"
        verbose_name_plural = "5.5. image ticket list"

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="Ticket")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.ticket.name}"

#6
class Packet(models.Model):
    class Meta:
        db_table = "packet"
        verbose_name_plural = "6. Packet" 
    
    category = models.ForeignKey(CategoryModelPacket, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100, default="name")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField()
    address = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.name)    

class ImagePacketModel(models.Model):
    class Meta:
        db_table = "ImagePacketModel"
        verbose_name_plural = "6.6. image packet list"

    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, verbose_name="Packet")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.packet.name}"

#7
class Guide(models.Model):
    class Meta:
        db_table = "guide"
        verbose_name_plural = "7. Guide" 
    
    category = models.ForeignKey(CategoryModelGuide, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    address = models.TextField()

    def __str__(self):
        return str(self.name)

class ImageGuideModel(models.Model):
    class Meta:
        db_table = "ImageGuideModel"
        verbose_name_plural = "7.7. image guide list"

    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, verbose_name="Guide")
    image = models.FileField(null=True, blank=True, verbose_name="image", upload_to="media/")

    def __str__(self):
        return f"Image for {self.guide.name}"

