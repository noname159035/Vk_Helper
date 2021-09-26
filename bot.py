#!/usr/bin/python3.7
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import speech_recognition
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import pymongo
from pymongo import MongoClient
import time
import pyowm
import math
import datetime
from datetime import datetime, timedelta
import urllib.request
import bs4
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
import datetime
import threading

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

from auto_message import *
from news_methods import *

def start_helper():
    get_text("Да-Да")
    # while True:
    #     with m as source:
    #         audio = r.listen(source)
    #     callback(r, audio)


def start_bot():
    while True:
        pass


get_text("ЗАГРУЗКА СЛОВАРЕЙ...")
print("ЗАГРУЗКА СЛОВАРЕЙ...")
text = {
    "максим" : "?",
    "макс" : "?",
    "сись" : "?",
    "сисечка" : "?",
    "сиська" : "?",
    "саси" : 'ой, да иди ты уже нахуй',
    "соси" : 'ой, да иди ты уже нахуй',
    "пошёл в жопу" : 'Ебать ты оригинальный',
    "пошел в жопу" : 'Ебать ты оригинальный',
    "пошел нахуй" : 'Ебать ты оригинальный',
    "пошёл нахуй" : 'Ебать ты оригинальный',
    "пошёл на хуй" : 'Ебать ты оригинальный',
    "пошел на хуй" : 'Ебать ты оригинальный',
    "как дела?" : 'Неплохо, а ты как',
    "как жизнь?": 'Неплохо, а ты как',
    "как учеба?": 'Неплохо, а ты как',

    "привет, как дела?": 'Неплохо, а ты как',
    "привет, как жизнь?": 'Неплохо, а ты как',
    "привет, как учеба?": 'Неплохо, а ты как',
    "споки" : 'споки❤',
    "спокойной ночи" : 'споки❤',
    "привет": "привет"
}

opts = {
        "alias": ("саня", "саша", "александр", "сань"),  # имена
        "tbr": ("скажи", "расскажи "),  # комманды которые удаляются для понимания команды
    }

cmds = {
    "tell": ('отправь сообщение', "напиши", "ответь", "напиши сообщение"),
}


get_text("СЛОВАРИ ЗАГРУЖЕНЫ УСПЕШНО...")
print("СЛОВАРИ ЗАГРУЖЕНЫ УСПЕШНО...")
login, password = "####", "#####"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)
vk = vk_session.get_api()

now = datetime.datetime.today()

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# r = sr.Recognizer()
# m = sr.Microphone(device_index=1)
# engine = pyttsx3.init()
#
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)

alarm = 0
get_text("ЗАПУСК...")
print("ЗАПУСК...")
kol = 0

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            print('Сообщение пришло в: ' + str(now.strftime("%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print("Отправитель: " + str(event.user_id))
            print("")

            response = event.text.lower()
            response2 = response[6:len(response)]
            beg = response[0:6]

            get_text(get_name(event.user_id) + "написал:," + response)

            try:
                if event.from_user:
                    print("говори")
                    to_do = hear()

                    if to_do == "не отвечай" or to_do == "не пиши":
                        pass

                    elif to_do == "ответь" or to_do == "напиши" or to_do == "игнорируй" or to_do == "":
                        print("говори")
                        mes = hear()
                        print("отправляю " + mes)
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': mes, 'random_id': 0})

            except speech_recognition.UnknownValueError as e:
                print("[log] Речь не была распознана")


        def get_attachment(attachment):
            if event.from_user:
                vk_session.method('messages.send',
                                  {'user_id': event.user_id, 'message': 'Держи мой сладкий', 'random_id': 0,
                                   "attachment": attachment})
            elif event.from_chat:
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id, 'message': 'Держи мой сладкий', 'random_id': 0,
                                   "attachment": attachment})


        if response in text:
            if event.from_user:
                vk_session.method('messages.send',
                                  {'user_id': event.user_id,
                                   'message': text[response], 'random_id': 0})
            elif event.from_chat:
                vk_session.method('messages.send',
                                  {'chat_id': event.chat_id,
                                   'message': text[response], 'random_id': 0})

# threading.Thread(target=start_bot).start()
# threading.Thread(target=start_helper).start()



