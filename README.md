# EPL-Django-App

in progress 01/10/2023

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/static/v1?style=for-the-badge&message=HTML5&color=E34F26&logo=HTML5&logoColor=FFFFFF&label=)
![CSS3](https://img.shields.io/static/v1?style=for-the-badge&message=CSS3&color=1572B6&logo=CSS3&logoColor=FFFFFF&label=)
![Bootstrap](https://img.shields.io/static/v1?style=for-the-badge&message=Bootstrap&color=7952B3&logo=Bootstrap&logoColor=FFFFFF&label=)

<p float="left">
<img src="https://drive.google.com/uc?export=view&id=1Ja0kDFlFVkaOUeVWXRe4xdPieUBcrqmy" width="40%" height="40%" />
<img src="https://drive.google.com/uc?export=view&id=1KYuaB0yi5Wf-4LvCkX0stImbMQXS5QHy" width="40%" height="40%" />
</p>

## What is it?

- I love soccer so much and keep up with English Premier League. So I wanted to get the EPL information with public API
- Information from API will be saved or updated in database
- Models: Players, Teams, Matches, Scores
- Built RESTful APIs
- Users can register/login and save their Favorite Team

## Functionality

- Django Web Application
- Django Rest Framework
- Restful API

```
  (only admin can view profiles)
  "GET": "/api/profiles",
  "GET": "/api/profiles/id",

  "GET": "/api/teams"
  "GET": "/api/teams/teamnumber"

  "GET": "/api/matches"
  "GET": "/api/matches/matchdays/matchday"
  "GET": "/api/matches/matchcode"
  "GET": "/api/matches/matchcode/scores"

  "GET": "/api/leaderboard"
  "GET": "/api/top-scorer"

  "GET": "/api/players"
  "GET": "/api/players/playercode"

  "POST": "/api/profiles/id/favteam/add/"
  "PATCH": "/api/profiles/id/favteam/remove/"
```

## Postman

<p float="left">
<h5><img src="https://drive.google.com/uc?export=view&id=1Q-u-8Fjhpv61b5PumAxIW6KLcyqT_6Ox" width="40%" height="50%" />
['GET']Get all EPL teams in DB</h5>
<h5><img src="https://drive.google.com/uc?export=view&id=1kJPKet_0MaufOAokeGFQI5bzq2DsbP2x" width="40%" height="50%" />
['GET']Get a specific Team by Teamnumber (Tottenham Hotspur)</h5>
<h5><img src="https://drive.google.com/uc?export=view&id=1UOTUZvEJt1Lc02xBnfENNIwZYCD7LUY6" width="40%" height="50%" />
['GET']Access to information denied due to Authentication failure</h5>
<h5><img src="https://drive.google.com/uc?export=view&id=12pAWbmd6L7fAv5FZvZBg4BR1brp8v8W0" width="40%" height="50%" />
['POST']Add Profile's Favorite Team by Team number</h5>
<h5><img src="https://drive.google.com/uc?export=view&id=1OMsUP4cd_jPr8DeixfQYveoWhvF73nV2" width="40%" height="50%" />
['PATCH']Remove Profile's Favorite Team</h5>
</p>

## Problems I faced

- Had trouble with Game outcomes. I found out that Null and Draw values were a thing for some games.
- The matches were not updating and I fixed it by using update_or_create and update for Objects.
