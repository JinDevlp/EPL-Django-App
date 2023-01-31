# EPL-Django-App

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
<img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" />


<p float="left">
<img src="https://drive.google.com/uc?export=view&id=1Ja0kDFlFVkaOUeVWXRe4xdPieUBcrqmy" width="45%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1KYuaB0yi5Wf-4LvCkX0stImbMQXS5QHy" width="45%" height="20%" />
</p>

## What is it?

- I love soccer so much and keep up with English Premier League. So I wanted to get the EPL information with public API
- Information from API will be saved or updated in Postgres Database
- Get access to EPL information that is saved in DB with REST APIs
- Users can register/login and save their Favorite Team

## Functionality

- Django Web Application
- Django Rest Framework
- REST API
- Authentication with JWT
- Only Admin can edit Users

| PATH  | HTTP Method | Outcome |
| :--- | :--- | :--- |
|GET| /users| LIST users|
|GET| /users/id| READ user|
|POST| /users| CREATE user| 
|PUT| /users/id| UPDATE user|
|DELETE| /users/id| DELETE user|
|GET| /profiles | LIST profiles|
|GET| /profiles/id | READ profile|
|GET| /teams| LIST teams|
|GET| /teams/id| READ team|
|GET| /players| LIST players|
|GET| /players/id| READ player|
|GET| /leaderboard| LIST leaderboard|
|GET| /top-scorer|LIST top scorers in EPL league|
|GET| /matches| LIST matches in EPL league|
|GET| /matches/id| READ match by ID|
|GET| /matches/matchdays/matchday| READ match by matchday|

## Problems I faced

- I was overwhelmed by the amount of data that I got back from the public API. I broke it down with searching by ID and began to route my path.
- Had trouble with Game outcomes. I found out that Null and Draw values were a thing for some games.
- Public API had lots of Json values which I wasn't aware of. Such as game being "scheduled" or "postponed". Solved it by inspecting what was not being recorded with my code and checking Json Data from public api.


## Postman

<p float="left">

<img src="https://drive.google.com/uc?export=view&id=1A32bNaV6uMOtc5tiM3HXJAz2JNY0rViK" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1M7kDE1idlpHJXFIxJwp2obeVB1q3oj5D" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1h3Gfg8lSDf1oU_mJYjmO95SYK0G1LfSZ" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1YTTMHXr8jGfioDOjJ2l9WyseixaunK55" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1e6a5ZXPDQUFAeeYHY0fiPh8gl4o6bN8i" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1RmYuFxR89GIZ6rbqLbDcZm7x89z-X6oc" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1Q-u-8Fjhpv61b5PumAxIW6KLcyqT_6Ox" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1kJPKet_0MaufOAokeGFQI5bzq2DsbP2x" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1UOTUZvEJt1Lc02xBnfENNIwZYCD7LUY6" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=12pAWbmd6L7fAv5FZvZBg4BR1brp8v8W0" width="40%" height="50%" />
<img src="https://drive.google.com/uc?export=view&id=1OMsUP4cd_jPr8DeixfQYveoWhvF73nV2" width="40%" height="50%" />
</p>
