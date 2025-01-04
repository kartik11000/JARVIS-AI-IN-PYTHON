import requests
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia as wk
import webbrowser
import os
import smtplib
from bs4 import  BeautifulSoup
import pywhatkit
import pyautogui
import pyowm
import keyboard
import time 
import openai
from datetime import timedelta


import random




from time import sleep



# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def hello ():
    hour = int(datetime.datetime.now().hour)
    if"hello jaan"in query():
        hour >= 0 and hour < 12
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am,NIKITA")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=800
        audio = r.listen(source, 0,4)

    try:
        print("under standing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again")
        return "None"

    return query


if __name__ == "__main__":
    while True:
        query=take_command().lower()
        if "go to sleep"in query:
            speak("ok kartik ,you can me call any time")
            break
        elif"hello"in query:
            speak("hello kartik,how are you")
        elif"i am fine"in query:
            speak("that 's great kartik") 
        elif"how are you" in query:
            speak("perfact, kartik")
        elif"thank you " in query:
            speak("you are welcome ,kartik")
        elif"now time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:S")
            speak(f"kartik,the time is{strtime}")
        elif "youtube" in query:
            from search import searchyoutube
            searchyoutube(query)
        elif "wikipedia" in query:
            from search import searchwikipedia
            searchwikipedia(query)
        elif "google" in query:
            from search import searchGoogle
            searchGoogle(query)
        elif"open" in query:
            from web import openappweb
            openappweb(query)
        elif"close" in query:
            from web import closeappweb
            closeappweb(query)
        elif "temperature"in query:
            search="temperature in dhoondly"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current{search}is {temp}")
            print(f"current{search}is {temp}")
        elif "weather"in query:
            search="temperature in dhoondly"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current{search}is {temp}")
            print(f"current{search}is {temp}")

        elif "the time " in query:
            replace=query.replace("jarvis")
            replace=query.replace("the")
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sie,the time is {strtime}")


        elif "volume up" in query:
           from keyboard import volumeup
           volumeup(query)
           speak("volume up")

        elif "volume down" in query:
             from keyboard import volumedown
             volumedown(query)
             speak("volume down")
            
        elif"pause" in query:
            pyautogui.press("k")
            speak("video pause")

        elif"play" in query:
            pyautogui.press("k")
            speak("video is play")
            
        elif"mute" in query:
            pyautogui.press("m")
            speak("video is mute")

        elif"send message" in query:
            from whatsapp import sendmassage
            sendmassage(query)
        

        elif"remember that " in query:
            rememberMassage=query.replace("remember that","")
            rememberMassage= query.replace("jarvis","")
            remember= open("remember.text","w")
            remember.write(rememberMassage)
            remember.close()

        elif" what do you remember" in query:
             replace=query.replace("what do you remember","")
             replace=query.replace("jarvis","")
             replace=query.replace("remember","")
             remember=open("remember.text","r")
             speak("you told me "+remember.read())

       

        elif"news" in query:
            from kam import openait
            openait(query)
            speak("ai is open")



     
           
           
       

            

               