from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import LoginView
from .views import *  


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('home/', queue_counter, name='home'),  # Name it appropriately. 'home' is just a suggestion.
]