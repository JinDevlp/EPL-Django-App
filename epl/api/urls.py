from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('teams', views.TeamsList.as_view(), name='teamsAPI' ),
    path('teams/<str:pk>',views.TeamsDetail.as_view(),name='teamAPI'),

    path('register/',views.CreateUserView.as_view()),

    path('leaderboard/', views.viewBoard),
    path('top-scorer/', views.viewTopScorers ),

    path('players', views.viewPlayers ),
    path('players/<str:pk>', views.viewPlayer ),

    path('matches', views.viewMatches),
    path('matches/days/<str:day>', views.viewMatch),
    path('matches/<str:pk>', views.viewMatch),
    path('matches/<str:pk>/scores', views.viewMatchScores),
    path('matches/matchdays/<str:pk>', views.matchDay),

    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<str:pk>', views.ProfileDetail.as_view()),

    path('profiles/<str:pk>/favteam/add/',views.addFavTeam),
    path('profiles/<str:pk>/favteam/remove/',views.removeFavTeam),
]

