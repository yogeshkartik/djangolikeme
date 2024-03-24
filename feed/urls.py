
from django.urls import path
from .views import feed

urlpatterns = [
    # path('/redirect/', createuser)
    path('/feed/', feed),
    # ... more URL patterns here
]