from django.shortcuts import render, redirect, get_object_or_404
from .models import Spot, Booking
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Spot, Booking


def spots(request):
    spots_list = Spot.objects.all()
    count = spots_list.count()
    return render(request, "bookings/spots.html", {
        "spots": spots_list,
        "count": count
    })


def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('bookings:spots')
    else:
        form = RegisterForm()
    return render(request, 'account/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":

        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('bookings:spots')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('bookings:account_login')


@login_required
def spot_detail(request, slug):
    spot = get_object_or_404(Spot, slug=slug)
    success = False

    if request.method == "POST":
        date = request.POST.get('date')
        if date:
            Booking.objects.create(customer=request.user, spot=spot, date=date)
            spot.status = Spot.Status.BUSY
            spot.save()
            success = True

    return render(request, "bookings/spot_detail.html", {
        "spot": spot,
        "success": success
    })


@login_required
def booking(request):
    if request.user.is_superuser and request.GET.get('reset') == 'true':
        Spot.objects.all().update(status=Spot.Status.AVAILABLE)
        Booking.objects.all().delete()
        return redirect('bookings:spots')

    user_bookings = Booking.objects.filter(customer=request.user)
    return render(request, "bookings/bookings.html", {"bookings": user_bookings})
