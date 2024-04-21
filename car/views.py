from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from car.forms import CustomUserLoginForm, CustomUserRegistrationForm, SearchForm, CommentForm
from car.models import Cars, Manufacturer, CommentModel


def cars(request):
    get = Cars.objects.all()
    brands = Manufacturer.objects.all()
    comments = CommentModel.objects.all()
    return render(request, "cars.html", {'cars': get, 'comments': comments, 'brands': brands})


def get_by_id(request, pk):
    get = Cars.objects.get(pk=pk)
    return render(request, "car-details.html", {"car": get})


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_cars')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class ImageCreateView(CreateView):
    model = Cars
    fields = []
    template_name = 'create_car.html'
    success_url = reverse_lazy('all_cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturer'] = Manufacturer.objects.all()
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            car_name = self.request.POST.get('car_name')
            car_manufacturer = self.request.POST.get('car_manufacturer')
            car_year = self.request.POST.get('car_year')
            car_description = self.request.POST.get('car_description')
            km = self.request.POST.get("km")
            car_fuel = self.request.POST.get("car_fuel")
            car_gearbox = self.request.POST.get("car_gearbox")
            car_number = self.request.POST.get("car_number")
            car_color = self.request.POST.get("car_color")
            car_price = self.request.POST.get("car_price")
            made_in = self.request.POST.get("made_in")
            car_image = self.request.FILES.get('car_image')
            if car_name and car_manufacturer and car_year and car_description and km and car_fuel \
                    and car_gearbox and car_number and car_color and car_price and made_in and car_image:
                form.instance.car_name = car_name
                car_manufacturer_instance = Manufacturer.objects.get(pk=car_manufacturer)
                form.instance.car_manufacturer = car_manufacturer_instance
                form.instance.car_year = car_year
                form.instance.car_user = self.request.user
                form.instance.car_description = car_description
                form.instance.km = km
                form.instance.car_fuel = car_fuel
                form.instance.car_gearbox = car_gearbox
                form.instance.car_number = car_number
                form.instance.car_color = car_color
                form.instance.car_price = car_price
                form.instance.made_in = made_in
                form.instance.car_image = car_image
            else:
                return self.form_invalid(form)
            form.save()
            return super().form_valid(form)
        else:
            return redirect('login')


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('car_name').capitalize()
            results = Cars.objects.filter(car_name=query)
            return render(request, 'search.html', {'search': results})
    return render(request, 'cars.html', {'form': None})


def add_comment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                user_comment = form.cleaned_data['user_comment']
                user_living_place = form.cleaned_data['user_living_place']
                CommentModel.objects.create(user=request.user, user_comment=user_comment, user_living_place=user_living_place)
                return redirect('all_cars')
        else:
            form = CommentForm()
        return render(request, 'add-comment.html', {'form': form})
    else:
        return redirect("login")


def brands(request,pk):
    brand = Cars.objects.filter(car_manufacturer=pk)
    return render(request,'search.html',{'brands':brand})
