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

    path('teams', views.TeamsList.as_view(), name='teamsAPI'),
    path('teams/<str:pk>',views.TeamsDetail.as_view(),name='teamAPI'),


    path('leaderboard', views.LeaderboardList.as_view()),
    path('top-scorer', views.TopScorerList.as_view() ),

    path('players', views.PlayersList.as_view() ),
    path('players/<str:pk>', views.PlayersDetail.as_view() ),

    path('matches', views.MatchesList.as_view()),
    path('matches/<str:pk>', views.MatchDetail.as_view()),
    path('matches/matchdays/<str:pk>', views.matchDay),

    path('profiles', views.ProfileList.as_view()),
    path('profiles/<str:pk>', views.ProfileDetail.as_view()),
    path('users', views.UserList.as_view()),
    path('users/<str:pk>', views.UserDetail.as_view()),

]

