import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser

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



query =take_command().lower()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)



def speak(audio):
 engine.say(audio)
 engine.runAndWait()



def searchGoogle(query):
    if"google" in query:
        import wikipedia as googleScrap
        query=query.replace("javis","")
        query=query.replace("google search","")
        speak("this is what i found on google")
        try:
           pywhatkit.search(query)
           result= googleScrap.summary(query,1)
           speak(result)
        

        except:
            speak("no speakable output available")





def searchyoutube(query):
    if"youtube" in query:
        speak("this is what i found for your search ")
        query=query.replace("jarvis","")
        query=query.replace("youtube search","")
        query=query.replace("youtube","")
        
        web= "https://www.youtube.com/results?search_query=" +query

        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done sir")



def searchwikipedia(query):
    if "wikipedia"in query:
        speak("search for wikipedia.....")
        query=query.replace("wikipedia","")
        query=query.replace("search wikipedia","")
        query=query.replace("javis","")

        result=wikipedia.summary(query,sentences=2)
        speak("according for wikipedia...")
        speak(result)
        print(result)


 

