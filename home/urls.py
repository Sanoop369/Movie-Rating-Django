from django.urls import path,include
from . views import *
app_name="home"
urlpatterns = [
   
    path('admin_sec',admin_home,name="admin_home"),
    path('movie_add',add_movie),
    path('movie_list',admin_movie_list,name="movie_list"),
    path('edit_movie/<str:pk>',edit_movie,name="editmovie"),
    path('delete_movie/<str:pk>',delete_movie,name="delete_movie"),
     path('genre_add',add_genre),
    path('genre_list',admin_genre_list,name="genre_list"),
    path('edit_genre/<str:pk>',edit_genre,name="editgenre"),
    path('delete_genre/<str:pk>',delete_genre,name="delete_genre"),
    path('admin_login',admin_signin,name="admin_login"),
    path('admin_logout',admin_logout,name="ad-logout"),
    path('login',login,name="login"),
    path('register',register,name="register"),
    path('',index,name="index"),
    path('allgenre',allgenre,name="allgenre"),
    path('genremovies',selectgenre),
    path('search',searchresult),
    path('allmovies',allmovies,name="allmovies"),
    path('movie-detail/<str:pk>',moviedetail,name="movie-detail"),
    path('logout',logout),
    path('watchlist',watchlist),
    path('add_watchlist/<str:pk>',add_watchlist)
]
