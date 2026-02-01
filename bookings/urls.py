from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "bookings"

urlpatterns = [
    path("", views.spots, name="spots"),
    path("signup/", views.signup_view, name="account_signup"),
    path("login/", views.login_view, name="account_login"),
    path("logout/", views.logout_view, name="account_logout"),
    path("spot/<slug:slug>/", views.spot_detail, name="spot_detail"),
    path("my-bookings/", views.booking, name="booking"),
]
