# Generated by Django 5.0.4 on 2024-04-19 09:56

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=55)),
                ('manufacturer_image', models.FileField(upload_to='manufacturer_image')),
            ],
            options={
                'verbose_name': 'Manufacture',
                'verbose_name_plural': 'Manufactures',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('user_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('None', 'None')], default='None', max_length=7)),
                ('groups', models.ManyToManyField(related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_user_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_year', models.IntegerField()),
                ('car_description', models.TextField()),
                ('km', models.IntegerField(default=0)),
                ('car_fuel', models.CharField(default='Petrol', max_length=25)),
                ('car_gearbox', models.CharField(default=None, max_length=25)),
                ('car_number', models.CharField(max_length=8, null=True, unique=True)),
                ('car_color', models.CharField(max_length=50)),
                ('car_price', models.DecimalField(decimal_places=3, max_digits=255)),
                ('made_in', models.CharField(max_length=30)),
                ('car_image', models.FileField(upload_to='cars_images')),
                ('car_created_at', models.DateTimeField(auto_now_add=True)),
                ('car_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.manufacturer')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars ',
            },
        ),
    ]
