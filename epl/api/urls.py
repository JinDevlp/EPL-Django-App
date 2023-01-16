from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('teams/', views.viewTeams, name='teams' ),
    path('teams/<str:pk>',views.viewTeam,name='team'),

    path('leaderboard/', views.viewBoard),
    path('top-scorer/', views.viewTopScorers ),

    path('players/', views.viewPlayers ),
    path('players/<str:pk>', views.viewPlayer ),

    path('matches/', views.viewMatches),
    path('matches/<str:pk>', views.viewMatch),

]

