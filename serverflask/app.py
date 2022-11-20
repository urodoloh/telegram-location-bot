import os
from unicodedata import name
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

load_dotenv()  # loads variables from .env file into environment

app = Flask(__name__)
CORS(app)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)

# CREATE TABLES
CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS users (user_id INT NOT NULL, user_name VARCHAR(255) NOT NULL, user_login_key VARCHAR(255) NOT NULL, PRIMARY KEY(user_id));"
CREATE_THEGAME_TABLE = "CREATE TABLE IF NOT EXISTS thegame (game_id INT GENERATED ALWAYS AS IDENTITY, user_id INT, latitude FLOAT NOT NULL, longitude FLOAT NOT NULL, status TEXT, date TIMESTAMP, PRIMARY KEY(game_id), CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE);"

# INSERT INTO TABLES
INSERT_USERS = "INSERT INTO users (user_id, user_name, user_login_key) VALUES (%s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET user_name = (%s)"
INSERT_THEGAMEDATA = "INSERT INTO thegame (user_id, latitude, longitude, status, date) VALUES (%s, %s, %s, %s, current_timestamp);"

# GET ALL DATA FROM TABLE
GET_USERLIST_FROM_USERS_TABLE = "SELECT user_id, user_name FROM users"
GET_GAMELIST_FROM_THEGAME_TABLE = "SELECT * FROM thegame"
# GET BY ID
GET_USERBYID_FROM_USERS_TABLE = (
    "SELECT user_id, user_name FROM users WHERE user_id = (%s)"
)
GET_GAME_BYUSERID_FROM_THEGAME_TABLE = "SELECT * FROM thegame WHERE user_id = (%s)"
GET_GAMES_IN_PROGRESS_WHERE_USER_ID_FROM_THE_GAME = (
    "SELECT * FROM thegame WHERE user_id = (%s) AND status = 'in_progress' LIMIT 10"
)
GET_ENDED_GAMES_FROM_THEGAME_TABLE = "SELECT users.user_id, user_name, thegame.status, thegame.date FROM users RIGHT OUTER JOIN thegame ON users.user_id = thegame.user_id WHERE status = 'done'"
GET_ENDED_GAMES_WHERE_USER_ID_FROM_THEGAME = (
    "SELECT * FROM thegame WHERE user_id = (%s) AND status = 'done'"
)
# PUT BY ID
UPDATE_THEGAMEDATA_BY_USERID = "UPDATE thegame SET status = (%s) WHERE user_id = (%s)"

# DELETE
DELETE_ALL_TABLES = "DROP TABLE users, thegame"
DELETE_TABLE_USERS = "DROP TABLE users CASCADE"
DELETE_TABLE_THEGAME = "DROP TABLE thegame"
# DELETE BY ID
DELETE_USER_BY_ID_RETURN_USERNAME = (
    "DELETE FROM users WHERE user_id = (%s) RETURNING user_name CASCADE"
)
DELETE_GAME_BY_USER_ID_RETURN_USER_ID = "DELETE FROM thegame WHERE user_id = (%s) AND status = 'in_progress' RETURNING user_id"


# POST ROUTES>>>>>>>>>>>>>
# users - create
@app.post("/api/users")
def create_user():
    data = request.get_json()

    user_id = data["user_id"]
    user_name = data["user_name"]
    user_login_key = data["user_login_key"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(
                INSERT_USERS, (user_id, user_name, user_login_key, user_name)
            )

    return {
        "id": user_id,
        "message": f"User {user_name} with login_key {user_login_key} created.",
        "status": "ok",
    }, 201


# thegame - create
@app.post("/api/thegame")
def add_thegame():
    data = request.get_json()
    user_id = data["user_id"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    status = data["status"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_THEGAME_TABLE)

            cursor.execute(
                GET_GAMES_IN_PROGRESS_WHERE_USER_ID_FROM_THE_GAME,
                (user_id,),
            )

            games_in_progress = cursor.fetchall()

            if games_in_progress == []:
                cursor.execute(
                    INSERT_THEGAMEDATA, (user_id, latitude, longitude, status)
                )

    return {
        "message": "the game added",
        "latitude": latitude,
        "longitude": longitude,
        "status": status,
    }, 201


# GET ROUTES>>>>>>>
# all users user_id, user_name
@app.get("/api/users")
def get_userlist():
    with connection:
        with connection.cursor() as cursor:

            # cursor.execute(CREATE_USERS_TABLE)
            try:
                cursor.execute(GET_USERLIST_FROM_USERS_TABLE)
                userlist_data = cursor.fetchall()
                userlist = []
                for el in userlist_data:
                    list_el = list(el)
                    user_id = list_el[0]
                    user_name = list_el[1]
                    userlist.append({"user_id": user_id, "user_name": user_name})
                status_code = 200
            except:
                user_id = "404"
                user_name = "404"
                status_code = 404
    return {"userlist": userlist}, status_code


# users - get user by id
@app.get("/api/users/<int:user_id>")
def get_user_by_user_id(user_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)

            try:
                cursor.execute(GET_USERBYID_FROM_USERS_TABLE, (user_id,))
                id = cursor.fetchone()[0]

                cursor.execute(GET_USERBYID_FROM_USERS_TABLE, (user_id,))
                name = cursor.fetchone()[1]

                # cursor.execute(GET_USERBYID_FROM_USERS_TABLE, (user_id,))
                # login_key = cursor.fetchone()[2]
            except:
                id = []
                name = []
                # login_key = []

    return {"user_id": id, "name": name}, 200


# get ended games with users
@app.get("/api/thegame")
def get_users_with_their_score():
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(GET_ENDED_GAMES_FROM_THEGAME_TABLE)
                thegames_data = cursor.fetchall()
                thegames = []
                for el in thegames_data:
                    list_el = list(el)
                    user_id = list_el[0]
                    user_name = list_el[1]
                    status = list_el[2]
                    date = list_el[3]
                    thegames.append(
                        {"user_id": user_id, "user_name": user_name, "status": status, "date": date}
                    )
                status_code = 200
            except:
                thegames = []
                user_id = None
                user_name = None
                status = None
                date = None
                thegames.append(
                    {"user_id": user_id, "user_name": user_name, "status": status, "date": date}
                )
                status_code = 404
    return thegames, status_code


# user_score_check and
@app.get("/api/thegame/<int:user_id>")
def get_ended_games(user_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_THEGAME_TABLE)
            try:
                cursor.execute(
                    GET_ENDED_GAMES_WHERE_USER_ID_FROM_THEGAME,
                    (user_id,),
                )
                ended_games = len(cursor.fetchall())
            except:
                ended_games = 0

            try:
                cursor.execute(
                    GET_GAMES_IN_PROGRESS_WHERE_USER_ID_FROM_THE_GAME,
                    (user_id,),
                )
                latitude = cursor.fetchone()[2]
                cursor.execute(
                    GET_GAMES_IN_PROGRESS_WHERE_USER_ID_FROM_THE_GAME,
                    (user_id,),
                )
                longitude = cursor.fetchone()[3]
                message = "all works"
            except:
                latitude = 0.0
                longitude = 0.0
                message = "table or id not exists"

    return {
        "score": ended_games,
        "latitude": latitude,
        "longitude": longitude,
        "message": message,
    }


# PUT ROUTES>>>>>>>>>>>>>>>>>
# thegame - put game status by user id
@app.put("/api/thegame/<int:user_id>")
def update_game__by_user_id(user_id):
    data = request.get_json()
    status = data["status"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_THEGAME_TABLE)

            try:
                cursor.execute(
                    UPDATE_THEGAMEDATA_BY_USERID,
                    (
                        status,
                        user_id,
                    ),
                )
                message = f"game status has been updated for user: {user_id}"
            except:
                message = "table thegame not exists"

    return {"message": message, "status": status}, 200


# DELETE ROUTES>>>>>>>>>>>>>>>
# delete all tables
@app.delete("/api")
def delete_all_tables():
    with connection:
        with connection.cursor() as cursor:

            try:
                cursor.execute(DELETE_ALL_TABLES)
                message = "all tables deleted"
            except:
                message = "some of the tables no longer exist"

    return {"message": message}, 200


# delete users
@app.delete("/api/users")
def delete_users_table():
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(DELETE_TABLE_USERS)
                message = "table users has been deleted"
            except:
                message = "table not exists"

    return {"message": message}, 200


# delete thegame
@app.delete("/api/thegame")
def delete_thegame_table():
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(DELETE_TABLE_THEGAME)
                message = "table thegame has been deleted"
            except:
                message = "table not exists"

    return {"message": message}, 200


# delete - user by id
@app.delete("/api/users/<int:user_id>")
def delete_user_by_id(user_id):
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(DELETE_USER_BY_ID_RETURN_USERNAME, (user_id,))
                user_name = cursor.fetchone()[0]
                message = "user has been deleted"
            except:
                message = "user not exists"
                user_name = user_id

    return {message: user_name}, 200


# delete - thegame by user_id
@app.delete("/api/thegame/<int:user_id>")
def delete_game_by_id(user_id):
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(DELETE_GAME_BY_USER_ID_RETURN_USER_ID, (user_id,))
                message = f"game has been deleted by {user_id}"
            except:
                message = f"user_id {user_id} not exists"

    return {"message": message}, 200
