# 404-project

## Frontend
React
library: axios, redux
structure: index.js, app.js /pages, /components, /assets

Services:
1. Login: call /auth/, frontend passes the username and password to the backend, then backend returns a token. frontend uses redux to store the user's token when user login.
2. Register: call /api/users/ to register and should also call /auth/ after register to get the token and save it into the redux.
3.  then send token with any request by extracting the token from redux.

## Backend
Django
library: Django REST framework

routes:
POST /auth/ => user login, return token
POST /api/users/ => user register, return None
