from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.adminLogin, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('searchUser/',views.searchUser, name='searchUser'),
    path('createUser/',views.createUser,name='createUser'),
    path('updateUser/<int:id>/',views.updateUser,name='updateUser'),
    path('deleteUser/<int:id>/',views.deleteUser, name='deleteUser'),
    path('logout/',views.adminLogout, name='adminLogout'),

]

