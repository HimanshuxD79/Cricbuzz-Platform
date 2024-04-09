
# Cricbuzz-like API Platform

This project is aimed at developing an API platform similar to Cricbuzz, allowing guest users to browse across multiple matches and view match details. It includes role-based access control with two types of users: Admins and Guests.


# Tech Stack
- Web Server: Django 
- Database: dbsqlite3 (Relational)

# Requirements
- Register Admin: Create an endpoint for registering a user as an admin.
- Login User: Provide the ability for users to log into their accounts.
- Create Match: Allow admins to add matches to the platform.
- Get Match Schedules: Provide an endpoint for guest users to fetch all match schedules.
- Get Match Details: Allow guest users to view details of a specific match.
- Add a Team Member to a Squad: Enable admins to add players to team squads.
- Get Player Statistics: Provide an endpoint for users to fetch player statistics.

# Setup and Installation
- Clone the repository
- Create Virtual environment and install dependencies
```
virtualenv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
pip install -r requirements.txt
```
# Run the development server.
```
python manage.py runserver
```
# API Endpoint
### Register Admin
- Endpoint: /api/admin/signup
- Method: POST
- Request Data:
```
{
    "username":"himanshu799",
    "email":"himanshu@gmail.com",
    "password":"ZAQmlp@00"
}
```
- Response 
```
{
    "status": "Account successfully created",
    "status_code": 201,
    "user_id": 7,
    "access_token": "52b71e301f13cdb7f8d600523804131e4f91dfa6"
}
```
### Login User
- Endpoint: /api/admin/login
- Method: POST
- Request Data:
```
{
    "username":"himanshu799",
    "password":"ZAQmlp@00"
}
```
- Response 
```
{
    "status": "Login successful",
    "status_code": 200,
    "user_id": 7,
    "access_token": "52b71e301f13cdb7f8d600523804131e4f91dfa6"
}
```
- Response Data for Failure:
```
{
  "status": "Incorrect username/password provided. Please retry",
  "status_code": 401
}

```

###  Create Match
- Endpoint: /api/addmatches
- Method: POST
- Request Data:
```
{
    "team_1": "India",
    "team_2": "Australia",
    "date": "2023-07-12",
    "venue": "Sydney Cricket Ground"
}
```
- Response 
```
{
    "message": "Match created successfully",
    "match_id": 24
}
```

###  Get Match Schedules
- Endpoint: /api/matches
- Method: POST


- Response 
```
"matches": [
        {
            "match_id": 1,
            "team_1_name": "India",
            "team_2_name": "Pakistan",
            "date": "2023-07-21",
            "venue": "SAC"
        },
        {
            "match_id": 2,
            "team_1_name": "India",
            "team_2_name": "Australia",
            "date": "2023-07-12",
            "venue": "Sydney Cricket Ground"
        }
]
```

###  Get Match Details
- Endpoint: /api/matches/{match_id}
- Method: POST


- Response 
```
{
    "match_id": 1,
    "team_1": {
        "name": "India"
    },
    "team_2": {
        "name": "Pakistan"
    },
    "date": "2023-07-21",
    "venue": "SAC",
    "status": "finished",
    "squads": {
        "team_1": [
            {
                "player": {
                    "player_id": "123",
                    "name": "Virat Kohli"
                }
            },
            {
                "player": {
                    "player_id": "126",
                    "name": "Rohit Sharma"
                }
            },
            {
                "player": {
                    "player_id": "126",
                    "name": "Rohit Sharma"
                }
            }
        ],
        "team_2": [
            {
                "player": {
                    "player_id": "124",
                    "name": "Babar azam"
                }
            },
            {
                "player": {
                    "player_id": "127",
                    "name": "Rohit Khatri"
                }
            }
        ]
    }
}
```
###  Add a Team Member to a Squad
- Endpoint: /api/teams/{team_id}/squad
- Method: POST
- Request Data:
```
{
    "name":"Rohit Sharma",
    "role":"Batsman"
}
```

- Response 
```
Response Data : {
 "message": "Player added to squad successfully",
 "player_id": "789"
 }
```
###  Get Player Statistics
- Endpoint: /api/players/{player_id}/stats
- Method: POST
- Response 
```
{
    "player_id": "123",
    "name": "Virat Kohli",
    "matches_played": 200,
    "runs": 12000,
    "average": 15.36,
    "strike_rate": 561.2
}
```

# Note 
## I have added some functionalities according to my assumption :
- During adding a player in squad , player with that name must be present in the players database table .
- For Better testing you can use django admin panel using 
```
py manage.py createsuperuser
# make your account then visit
127.0.0.1:8000/admin
```
and can add some dummy data.

