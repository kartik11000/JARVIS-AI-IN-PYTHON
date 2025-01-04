import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



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

strTime=int(datetime.now().strftime("%H")) 
update=datetime.datetime.now().strftime("%H:%M:S")



def sendmassage():
    speak("whon do you want to message")
    a=int (input('''person 1-1 person 2-2'''))
    if a==1:
        speak("whats the massage")
        message=str(input("enter the massage"))
        pywhatkit.sendwhatmsg("+91 7017634047",message,time_hour=strTime,time_min=update)

    elif a==2:
     speak("what the massage")
     message=str(input("enter the massage "))
     pywhatkit.sendwhatmsg("+919634849247",message,time_hour=strTime,time_min=update)
     try:
         speak("thanks for the message")
     except Exception as e:
         print("error")