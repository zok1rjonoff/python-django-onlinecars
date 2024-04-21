from django.contrib import admin
from .models import User, Manufacturer, Cars, CommentModel
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'phone_number', 'user_gender',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'user_gender',)}),
    )
    list_display = ['username', 'phone_number','password', 'user_gender', 'is_active', ]


admin.site.register(User, CustomUserAdmin)


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "user_comment",'user_living_place']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["pk", "manufacturer_name", "manufacturer_image"]
    search_fields = ["manufacturer_name"]
    ordering = ["manufacturer_name"]


@admin.register(Cars)
class AdminCars(admin.ModelAdmin):
    list_display = ["pk", "car_name", 'car_user', "car_manufacturer", "car_year", "car_description",
                    "car_number", "car_color", "car_price", "made_in", "car_image", "car_created_at"]
    search_fields = ["car_name", "car_year", "car_number"]
