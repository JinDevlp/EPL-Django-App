from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    # path('teams/<str:pk>',views.viewTeam,name='team')
]

