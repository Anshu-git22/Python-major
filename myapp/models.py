from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    usertype=(
        ("buyer","buyer"),
        ("seller","seller"),
    )
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.TextField()
    password=models.CharField(max_length=50)
    profile_picture=models.ImageField(upload_to="profile_picture/")
    user_type=models.CharField(max_length=50,choices=usertype)
    
    def __str__(self):
        return self.fname+" "+self.lname
    
class Product(models.Model):
    category=(
        ("Sports","Sports"),
        ("Sneakers","Sneakers"),
        ("Running Shoes","Running Shoes"),
    )
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    product_category=models.CharField(max_length=100,choices=category)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveIntegerField()
    product_desc=models.TextField()
    product_image=models.ImageField(upload_to="product_image/")

    def __str__(self):
        return self.seller.fname+" - "+self.product_name
    

class Wishlist(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    product_price=models.PositiveIntegerField()
    product_qty=models.PositiveIntegerField(default=1)
    total_price=models.PositiveIntegerField()
    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name