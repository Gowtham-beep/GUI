#this urls is to handle all the routing of the webpage
from django.urls import path
from . import views

urlpatterns=[
    
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerpage,name='register'),
    path('',views.home,name="home"),
    path('room/<int:pk>/',views.room,name="room"),
    path('user-profile/<int:pk>/',views.userProfile,name="user-profile"),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<int:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<int:pk>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<int:pk>/',views.deleteMessages,name='delete-message'),
    path('update-user/',views.updateUser,name='update-user'),
    path('topics/',views.topicspage,name='topics'),
    path('activities/',views.activitiespage,name='activities'),

]