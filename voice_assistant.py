import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
from datetime import datetime as date
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

y=date.today().strftime('%A')

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("today's day is")
    speak(y)

def takeCommand():
    "It takes microphone input from the user and returns string output"

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        r.pause_threshold = 1

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content ):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('geddadaraviteja612@gmail.com', 'ravihills7')
    server.sendmail('geddadaraviteja612@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    print("******************************************************")
    print("****         ANNA - THE TALKING COMPUTER          ****")
    print("***     ARTIFICIAL NETWORK AND NEURAL ABILITY      ***")
    print("**                2019 RAVI TEJA G                  **")
    print("******************************************************")

    wishMe()

    while True:

    # if 1:

        query = takeCommand().lower()
         #Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=7)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/webhp?authuser=1")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("whom should i send email?")
                to = takeCommand()
                speak("what should I say?")
                content = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'google news' in query:
            webbrowser.open("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
            speak("Today's top headlines in google news")
            url = (
                "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=ec79cedf57424d6391023e1d1574e3cb")
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for i in range(0, 7):
                speak(arts[i]['title'])

        elif 'anna' in query:
            speak("Iam anna Tell me How may i help you?")

