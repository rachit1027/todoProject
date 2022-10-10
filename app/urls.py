from django.contrib import admin
from django.urls import path
from app.views import home, signup,add_todo
from app.views import login,signout,delete_todo




urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup),
    path('add-todo/',add_todo),
    path('delete-todo/<int:id>',delete_todo),
    path('logout/',signout)
]
