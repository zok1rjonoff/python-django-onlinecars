from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cars, CommentModel


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')


class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UploadImage(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class SearchForm(forms.Form):
    car_name = forms.CharField()


class CommentForm(forms.Form):
    user_comment = forms.CharField(widget=forms.Textarea)
    user_living_place = forms.CharField()

