from home.views.home_view import HomeView
from home.views.about_view import about
from home.views.authenticated_view import authenticated
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('auth/', authenticated, name='auth'),
]
