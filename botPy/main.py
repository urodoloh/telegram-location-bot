from urllib import response

# formulas
from utils.numbers import *

# login key generator
import uuid

# telebot
from telebot import TeleBot, types

# States (for menu routing)
from telebot.handler_backends import State, StatesGroup

# States storage
from telebot.storage import StateMemoryStorage

# Storage init
state_storage = StateMemoryStorage()
import random


# Rest api things
import requests
import json


# server url
api_url = "http://localhost:5000/api/"


# bot object init
app = TeleBot(
    token="5426412733:AAG6272BW7o3A478pipnm8i8H1kBceG-YjA", state_storage=state_storage
)


# START
@app.message_handler(commands=["start"])
def start_command(message):
    chat = message.chat.id
    markup_reply_resize = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )

    # add BUTTONS
    markup_reply_resize.add(types.KeyboardButton("YES"), types.KeyboardButton("NO"))
    # helper handler (for new step)
    msg = app.send_message(
        chat,
        "HELLO BOY, IT'S A LOCATION GAME BOT. YOUR LOCATION WILL NOT BE SAVED. OKAY?",
        reply_markup=markup_reply_resize,
    )
    # next step handler
    app.register_next_step_handler(msg, user_answer)


def user_answer(message):
    chat = message.chat.id

    if message.text == "YES":
        msg = app.send_message(chat, "INTER YOUR NAME")
        app.register_next_step_handler(msg, user_registration)

    if message.text == "NO":
        app.send_message(chat, "no means no, okay :(")


# REGISTRATION
def user_registration(message):
    chat = message.chat.id
    user_name = message.text

    def postUserData():
        user_id = message.from_user.id
        user_login_key = str(uuid.uuid4())
        users_url = api_url + "users"
        payload = {
            "user_name": user_name,
            "user_id": user_id,
            "user_login_key": user_login_key,
        }
        response = requests.post(users_url, json=(payload))
        # response_json = response.json()
        # print(response_json["status"])
        if response.status_code == 201:
            app.send_message(
                chat,
                f"NAME {user_name} SAVED",
            )
        else:
            app.send_message(
                chat,
                f"YOUR ID ALREADY EXISTS. CLEAR THE DATABASE",
            )

    postUserData()

    markup_reply_resize = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    markup_reply_resize.add(
        types.KeyboardButton("START GAME"), types.KeyboardButton("OPTIONS")
    )

    msg = app.send_message(chat, "MENU", reply_markup=markup_reply_resize)
    app.register_next_step_handler(msg, menu_listener)


def menu_listener(message):
    if message.text == "START GAME":
        # add BUTTONS
        markup_reply_resize = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        markup_reply_resize.add(
            types.KeyboardButton("GIVE MY LOCATION", request_location=True)
        )

        msg = app.send_message(
            message.chat.id, "GIVE YOUR LOCATION", reply_markup=markup_reply_resize
        )

        app.register_next_step_handler(msg, start_the_game)

    if message.text == "OPTIONS":
        # add BUTTONS
        markup_reply_resize = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        markup_reply_resize.add(
            types.KeyboardButton("EDIT NAME"),
            types.KeyboardButton("SHOW MY SCORE"),
            types.KeyboardButton("GET ME MY LOGIN KEY"),
            types.KeyboardButton("GO TO LEADER BOARD PAGE"),
        )

        msg = app.send_message(
            message.chat.id, "SELECT OPTION", reply_markup=markup_reply_resize
        )
        app.register_next_step_handler(msg, options_menu_listener)


# GAME CREATING
def start_the_game(message):
    chat = message.chat.id
    coords = {}
    print("Starting game")
    if message.location:
        print("GIVE MY LOCATION")
        # init coords
        coords = {
            "latitude": message.location.latitude,
            "longitude": message.location.longitude,
        }
        # new coords
        random_distance = get_random_distance(10000, 11001)
        new_location = point_at_distance(coords, random_distance)
        coords["latitude"] = new_location["latitude"]
        coords["longitude"] = new_location["longitude"]
        print(new_location)
        app.send_message(
            chat,
            f"POINT CREATED",
        )

        def post_thegame_data():
            latitude = coords["latitude"]
            longitude = coords["longitude"]

            payload = {
                "user_id": message.from_user.id,
                "latitude": latitude,
                "longitude": longitude,
                "status": "in_progress",
            }

            thegame_url = api_url + "thegame"
            response = requests.post(thegame_url, json=(payload))

            if response.status_code == 201:
                app.send_message(
                    chat,
                    f"POINT SAVED. REACH THE POINT",
                )
                # add BUTTONS
                markup_reply_resize = types.ReplyKeyboardMarkup(
                    resize_keyboard=True, one_time_keyboard=True
                )
                markup_reply_resize.add(
                    types.KeyboardButton("CHECK LOCATION", request_location=True),
                    types.KeyboardButton("STOP THE GAME"),
                )

                msg = app.send_message(
                    chat,
                    "THE GAME HAS STARTED",
                    reply_markup=markup_reply_resize,
                )
                app.send_location(chat, coords["latitude"], coords["longitude"])

                app.register_next_step_handler(msg, game_process)

            if response.status_code == 500:
                app.send_message(
                    chat,
                    f"YOUR ID IS NOT EXISTS",
                )
                msg = app.send_message(chat, "INTER YOUR NAME")
                app.register_next_step_handler(msg, user_registration)

        post_thegame_data()


def game_process(message):
    chat = message.chat.id
    the_game_id_url = api_url + f"thegame/{message.from_user.id}"

    if message.text == "CHECK LOCATION":
        if message.location:
            user_current_coords = {
                "latitude": message.location.latitude,
                "longitude": message.location.longitude,
            }
            response = requests.get(the_game_id_url)
            response_json = response.json()

            game_current_point = {
                "latitude": response_json["latitude"],
                "longitude": response_json["longitude"],
            }
            # IF USER IN AREA
            if distance_between(user_current_coords, game_current_point) < 999:
                user_current_coords = {}
                # add buttons
                markup_reply_resize = types.ReplyKeyboardMarkup(
                    resize_keyboard=True, one_time_keyboard=True
                )
                markup_reply_resize.add(
                    types.KeyboardButton("START GAME"), types.KeyboardButton("OPTIONS")
                )

                msg = app.send_message(chat, "MENU", reply_markup=markup_reply_resize)
                app.register_next_step_handler(msg, menu_listener)

            # IFb
            #  USER NOT IN AREA
            if distance_between(user_current_coords, game_current_point) > 999:
                # add BUTTONS
                markup_reply_resize = types.ReplyKeyboardMarkup(
                    resize_keyboard=True, one_time_keyboard=True
                )
                markup_reply_resize.add(
                    types.KeyboardButton("CHECK LOCATION", request_location=True),
                    types.KeyboardButton("STOP THE GAME"),
                )

                msg = app.send_message(
                    chat, "GET CLOSER", reply_markup=markup_reply_resize
                )
                app.register_next_step_handler(msg, game_process)

    if message.text == "STOP THE GAME":
        response = requests.delete(the_game_id_url)
        return


def options_menu_listener(message):
    chat = message.chat.id
    if message.text == "EDIT NAME":
        msg = app.send_message(chat, "INTER NEW NAME")
        app.register_next_step_handler(msg, user_registration)

    if message.text == "SHOW MY SCORE":
        response = requests.get(api_url + f"thegame/{message.from_user.id}")
        response_json = response.json()
        result = response_json["result"]
        msg = app.send_message(chat, f"YOUR SCORE: {len(result)}")
        # add buttons
        markup_reply_resize = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        markup_reply_resize.add(
            types.KeyboardButton("START GAME"), types.KeyboardButton("OPTIONS")
        )
        # go to menu
        msg = app.send_message(chat, "MENU", reply_markup=markup_reply_resize)
        app.register_next_step_handler(msg, menu_listener)

    if message.text == "GET ME MY LOGIN KEY":
        response_get = requests.get(api_url + f"users/{message.from_user.id}")
        response_get_json = response_get.json()
        login_key = response_get_json["user_login_key"]
        app.send_message(chat, f"YOUR LOGIN KEY: {login_key}")

        # add buttons
        markup_reply_resize = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        markup_reply_resize.add(
            types.KeyboardButton("START GAME"), types.KeyboardButton("OPTIONS")
        )
        # go to menu
        msg = app.send_message(chat, "MENU", reply_markup=markup_reply_resize)
        app.register_next_step_handler(msg, menu_listener)

    if message.text == "GO TO LEADER BOARD PAGE":
        return

    if message.text == "BACK TO MENU":
        # add buttons
        markup_reply_resize = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        markup_reply_resize.add(
            types.KeyboardButton("START GAME"), types.KeyboardButton("OPTIONS")
        )
        # go to menu
        msg = app.send_message(chat, "MENU", reply_markup=markup_reply_resize)
        app.register_next_step_handler(msg, menu_listener)


# GETINFO
@app.message_handler(commands=["get info", "info"])
def get_user_info(message):
    chat = message.chat.id

    button_yes = types.InlineKeyboardButton(text="YES", callback_data="yes")
    button_no = types.InlineKeyboardButton(text="NO", callback_data="no")

    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(button_yes, button_no)

    app.send_message(chat, "get user info", reply_markup=markup_inline)


# after start YES/NO handler
@app.callback_query_handler(func=lambda call: True)
def answer_callback(call):
    if call.data == "yes":
        # add BUTTONS
        markup_reply_resize = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        markup_reply_resize.add(
            types.KeyboardButton("ID"),
            types.KeyboardButton("USERNAME"),
            types.KeyboardButton("ALL INFORMATION"),
        )

        app.send_message(
            call.message.chat.id, "select option:", reply_markup=markup_reply_resize
        )

    elif call.data == "no":
        app.send_message(call.message.chat.id, '"no" has been selected')


@app.message_handler(content_types=["text"])
def get_id_or_username(message):
    if message.text == "ID":
        app.send_message(message.chat.id, f"Your ID: {message.from_user.id}")
    elif message.text == "USERNAME":
        app.send_message(
            message.chat.id,
            f"Your Username: {message.from_user.first_name} {message.from_user.last_name}",
        )
    elif message.text == "ALL INFORMATION":
        app.send_message(message.chat.id, f"All your information: {message.from_user}")


app.enable_save_next_step_handlers(delay=2)
# app.load_next_step_handlers()
app.infinity_polling(skip_pending=True)
