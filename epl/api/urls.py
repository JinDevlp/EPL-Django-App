from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('teams/', views.TeamsList.as_view(), name='teamsAPI' ),
    path('teams/<str:pk>',views.viewTeam,name='teamAPI'),

    path('leaderboard/', views.viewBoard),
    path('top-scorer/', views.viewTopScorers ),

    path('players/', views.viewPlayers ),
    path('players/<str:pk>', views.viewPlayer ),

    path('matches/', views.viewMatches),
    path('matches/days/<str:day>', views.viewMatch),
    path('matches/<str:pk>', views.viewMatch),
    path('matches/<str:pk>/scores', views.viewMatchScores),
    path('matches/matchdays/<str:pk>', views.matchDay),

    path('profiles/', views.viewProfiles),
    path('profiles/<str:pk>', views.viewProfile),

    path('profiles/<str:pk>/favteam/add/',views.addFavTeam),
    path('profiles/<str:pk>/favteam/remove/',views.removeFavTeam),
]

