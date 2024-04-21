from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=55)
    manufacturer_image = models.FileField(upload_to="manufacturer_image")

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = "Manufacture"
        verbose_name_plural = "Manufactures"


class User(AbstractUser):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None'),
    )
    phone_number = models.CharField(max_length=13, unique=True)
    user_gender = models.CharField(max_length=7, choices=GENDERS, default='None')

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    objects = UserManager()


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comment = models.TextField()
    user_living_place = models.CharField(max_length=30)

    def __str__(self):
        return self.user_comment

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    car_year = models.IntegerField()
    car_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    car_description = models.TextField()
    km = models.IntegerField(null=False, default=0)
    car_fuel = models.CharField(default="Petrol", max_length=25)
    car_gearbox = models.CharField(null=False, max_length=25, default=None)
    car_number = models.CharField(max_length=8, unique=True, null=True)
    car_color = models.CharField(max_length=50)
    car_price = models.DecimalField(decimal_places=3, max_digits=255)
    made_in = models.CharField(max_length=50)
    car_image = models.FileField(upload_to="cars_images")
    car_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars "
