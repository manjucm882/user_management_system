from django.contrib import admin
from django.urls import path,include
from myapp.views import UserList,UserDetail

urlpatterns = [
    path('users/',UserList.as_view(),name='user-list'),
    path('user/<int:pk>/',UserDetail.as_view(),name='user-detail'),
]