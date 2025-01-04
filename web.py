import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
import speech_recognition as sr 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp={"commandprompt":"cmd","paint":"paint","word":"winword","excel":"execl","vs code":"vs code","powerpoint":"powerpnt"}
def  openappweb(query):
    speak("listing")
    if ".com" in query or ".co.in" in query or".org"in query:
        query=query.replace("open","")
        query=query.replace("lounch","")
        query=query.replace("webbrower ","")
        webbrowser.open(f"https//wwww.{query}")

    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dict[app]}")
def closeappweb(query):
    speak("closing ,kartik")
    if"one tab " in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif"2tab"in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif"3tab"in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif"4tab"in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif"5tab"in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill/f/in{dict[app]}.exe")
                
