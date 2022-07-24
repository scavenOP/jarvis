import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search


print("Initializing Jarvis")
MASTER = "Niladri"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',120)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Night" + MASTER)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('niladrisamanta4@niladri.com', '#error123456789')
    server.sendmail('niladrisamanta4@niladri.com', to, content)
    speak('sent')
    server.close()
speak("Initializing Jarvis")

if __name__ == "__main__":
    wishme()

    sendemail('niladris12345@gmail.com', 'I was sent through py.')
    # while True:

    #     query = takeCommand().lower()

    #     # for searching wikipedia
    #     if 'who is' in query:
    #         speak('Searching ...')
    #         query = query.replace("who is", "")
    #         results = wikipedia.summary(query, sentences=1)
            
    #         speak('According to Wikipedia')
    #         speak(results)

    #     elif 'email to niladri' in query:
    #         try:
    #             speak('What should i say ?')
    #             content = takeCommand()
    #             to = "niladris12345@gmail.com"
    #             sendemail(to, content)
    #             speak("Email has been sent!")
    #         except Exception as e:
    #             print(e)
    #             speak('Email not sent')

        

