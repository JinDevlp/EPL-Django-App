from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login' ),
    path('register/', views.register, name='register' ),
    path('logout/', views.logoutUser, name='logout' ),

    path('edit-profile/', views.editProfile, name='edit-profile' ),

]
