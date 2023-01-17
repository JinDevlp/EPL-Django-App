# EPL-Django-App

in progress 01/10/2023

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/static/v1?style=for-the-badge&message=HTML5&color=E34F26&logo=HTML5&logoColor=FFFFFF&label=)
![CSS3](https://img.shields.io/static/v1?style=for-the-badge&message=CSS3&color=1572B6&logo=CSS3&logoColor=FFFFFF&label=)
![Bootstrap](https://img.shields.io/static/v1?style=for-the-badge&message=Bootstrap&color=7952B3&logo=Bootstrap&logoColor=FFFFFF&label=)

<img src="https://drive.google.com/uc?export=view&id=1Ja0kDFlFVkaOUeVWXRe4xdPieUBcrqmy" width="50%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1KYuaB0yi5Wf-4LvCkX0stImbMQXS5QHy" width="50%" height="50%" />

## What is it?

- I love soccer so much and keep up with English Premier League. So I wanted to get the EPL information with public API
- Information from API will be saved or updated in database
- Models: Players, Teams, Matches, Scores
- Built RESTful APIs
- Users can register/login and save their Favorite Team

## Functionality

- Django Web Application
- Django REST API
- API
- (MODEL OBJECTS) -Serialization-> (PYTHON DICTIONARY) -Render into Json-> (JSON DATA)
- (JSON DATA) -ParseData-> (PYTHON NATIVE DATATYPE) -DeSerialization-> (COMPLEX DATATYPE)

```
  "GET": "/api/teams"
  "GET": "/api/teams/teamnumber"
  "GET": "/api/matches"
  "GET": "/api/matches/code"
  "GET": "/api/leaderboard"
  "GET": "/api/top-scorer"
  "GET": "/api/players"
  "GET": "/api/players/code"
```

## Problems I faced

- Had trouble with Game outcomes. I found out that Null and Draw values were a thing for some games.
- The matches were not updating and I fixed it by using update_or_create and update for Objects.
