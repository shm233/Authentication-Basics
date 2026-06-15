from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', signup_view, name="signup_view"),
    path('login/', login_view, name="login_view"),
    path('home/', homepage_view, name="homepage_view"),
    path('logout/', logout_view, name="logout_view"),
]
