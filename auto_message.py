import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {
    "alias": ("саня", "саша", "александр", "сань"), #имена
    "tbr": ("скажи", "расскажи "), #комманды которые удаляются для понимания команды
}

cmds = {
        "tell": ('отправь сообщение', "напиши", "ответь"),
    }

# функции

def get_text(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-Ru").lower()
        print("[log] Расспознано: " + voice)
        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts["alias"]:
                cmd = cmd.replace(x, "").strip()

            for x in opts["tbr"]:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd)

    except sr.UnknownValueError:
        print("[log] Непонял...")
    except sr.RequestError as e:
        print("[log] Чел, я не могу работать возможно интернет сдох")

def recognize_cmd(cmd):
    key = "no_find"
    try:
        for x in cmds:
            for i in range(len(cmds[x])):
                if cmds[x][i] == cmd:
                    key = x
    except UnboundLocalError as e:
        print("[log] неизвестная комманда")
        key = "no_find"

    return key


def execute_cmd(cmd):
    if cmd == "tell":
        get_text("хахахахахахахахахахаха")

    else:
        get_text("Я тебя не понял, повтори")

# запуск

r = sr.Recognizer()
m = sr.Microphone(device_index=1)
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def start_dialog():

    get_text("Да-Да")

    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, callback)
    time.sleep(15)

def hear():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)

    query = r.recognize_google(audio, language="ru-Ru")
    return query.lower()