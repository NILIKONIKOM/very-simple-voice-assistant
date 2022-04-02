import os
import speech_recognition as sr
import pyttsx3
import sys
import webbrowser
from bs4 import BeautifulSoup
import requests
from datetime import datetime, date, time
from random import randint

NumCommands = 0 #Number of commands executed

def talk(words):
    speak_engine = pyttsx3.init()
    voices = speak_engine.getProperty('voices')
    speak_engine.setProperty('voice', 'ru')
    speak_engine.say(words)
    speak_engine.runAndWait()
    speak_engine.stop()



def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        if NumCommands == 0:
            print("[log]: Говори")
            talk("Говори")

        elif NumCommands > 0:
            print("[log]: Скажи ещё что-нибудь")
            talk("Скажи ещё что-нибудь")

        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        quest = r.recognize_google(audio, language = "ru-RU").lower()
        print("Вы сказали: " + quest)

    except sr.UnknownValueError:
        talk("Я вас не понял")
        quest = command()

    return quest


def makeSomething(quest):
    if 'привет' in quest:
        mas = ['Приветствую!', 'Привет!', 'Здравствуй!']
        rand = randint(0,2)
        talk(mas[rand])
        print("[log]: " + str(mas[rand]))

    elif 'открой google' in quest:
        talk("Уже открываю")
        print("[log]: Уже открываю")
        url = 'https://google.com'
        webbrowser.open(url)

    elif 'стоп' in quest or 'stap' in quest:
        talk("Да, конечно, без проблем")
        print("[log]: Да, конечно, без проблем")
        sys.exit()

    elif 'время' in quest:
        time_checker = datetime.now()
        print('[log]: Сейчас ' + str(time_checker.hour) + ' ' + str(time_checker.minute))
        talk('Сейчас ' + str(time_checker.hour) + ' ' + str(time_checker.minute))

    elif 'доллар' in quest or 'долар' in quest:
        Dollar_rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83&aqs=chrome.4.69i57j35i39l2j69i59j0i131i433i512j69i61l3.4566j0j7&sourceid=chrome&ie=UTF-8"
        headers = {"User-Agent": " "} # your user agent
        full_page = requests.get(Dollar_rub, headers=headers)
        soup = BeautifulSoup(full_page.content, "html.parser")
        convert = soup.findAll("span", {"class": "DFlfde", "class":"SwHCTb", "data-precision": 2 })
        print("[log]: Сейчас доллар = " + convert[0].text + "руб.")
        talk("Сейчас доллар = " + convert[0].text + "руб.")

    elif 'евро' in quest or 'euro' in quest:
        euro_rub = "https://www.google.com/search?q=%D0%95%D0%B2%D1%80%D0%BE&oq=%D0%95%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i20i131i263i433i512j0i433i512j0i67i433j46i67i199i433i465j0i457i512j0i67j0i131i433i512j0i67i131i433j0i20i263i512.2007j1j7&sourceid=chrome&ie=UTF-8"
        headers = {"User-Agent": " "} # your user agent
        full_page = requests.get(euro_rub, headers=headers)
        soup = BeautifulSoup(full_page.content, "html.parser")
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        print("[log]: Сейчас евро = " + convert[0].text + "рублей.")
        talk("Сейчас евро = " + convert[0].text + "рублей.")


    elif 'найди в интернете' in quest or 'загугли' in quest or 'найди в google' in quest or 'найди в гугле' in quest:
        if 'найди в интернете' in quest:
            find = quest.split()
            find.remove('найди')
            find.remove('в')
            find.remove('интернете')
            find = ' '.join(find)
            url = 'http://www.google.com/search?q=' + str(find)
            webbrowser.open(url)
        elif 'загугли' in quest:
            find = quest.split()
            find.remove('загугли')
            find = ' '.join(find)
            url = 'http://www.google.com/search?q=' + str(find)
            webbrowser.open(url)
        elif 'найди в google' in quest:
            find = quest.split()
            find.remove('найди')
            find.remove('в')
            find.remove('google')
            find = ' '.join(find)
            url = 'http://www.google.com/search?q=' + str(find)
            webbrowser.open(url)
        elif 'найди в гугле' in quest:
            find = quest.split()
            find.remove('найди')
            find.remove('в')
            find.remove('гугле')
            find = ' '.join(find)
            url = 'http://www.google.com/search?q=' + str(find)
            webbrowser.open(url)

    else:
        print('[log]: Мне жаль, но у меня нет такой функции')
        talk('Мне жаль, но у меня нет такой функции')

if __name__ == '__main__':
    print("[log]: Привет, скажи мне что-нибудь.")
    talk("Привет, скажи мне что-нибудь.")
    while True:
        makeSomething(command())
        NumCommands+=1
