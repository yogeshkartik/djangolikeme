    # path('/redirect/', usersview.redirect_view),
from django.urls import path
from .views import createuser

urlpatterns = [
    # path('/redirect/', createuser)
    path('/create-user/', createuser)
    path('/login-user/', loginuser)
    path('/home/')
    # ... more URL patterns here
]