from django.shortcuts import render
import requests

import environ
env = environ.Env()
environ.Env.read_env()
# Create your views here.
def viewMatches(request):
    url = 'http://api.football-data.org/v4/competitions/PL/matches?season=2022'
    headers = { 'X-Auth-Token': env('TOKEN') }
    # matches json
    response = requests.get(url,headers=headers)
    matches_json = response.json()
    matches_list = matches_json['matches']

    return render(request, 'matches.html')