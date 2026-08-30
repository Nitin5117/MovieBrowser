from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('register/',views.registerUser,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),


    path('database/',views.dataBase,name="database"),
    path('profile/',views.profile,name="profile"),
    path('watchlist/<movie_id>/',views.watchlist,name="watchlist"),
    path('movieDetails/<movie_id>/',views.CastView,name='CastView')
    
]
