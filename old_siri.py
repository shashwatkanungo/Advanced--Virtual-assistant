import pyttsx3      # text to speech (speak())
import speech_recognition as sr    # speech to text (takecommand())
import datetime
import wikipedia
import webbrowser       #inbuilt module
import os
import random
import eel
from newsapi import NewsApiClient
from googletrans import Translator

from engine.features import *


# eel.init("www")

# playAssistantSound()

# os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# eel.start('index.html',mode =None, host='localhost', block=True)


newsapi = NewsApiClient(api_key = '512c2ff6579e4f8d89fffab00ee640ab')
api_key = '7aa79b45f13abb0e1f2c7a978a2371d4'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>= 12 and hour<18:
        speak('Good Afternoon!')
    
    else:
        speak('Good Evening')
    speak("I am Siri, I'm a virtual assistant here to make your life easier. How may I help you?")

def takeCommand():
    #it takes microphone input from user and return string as op

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query

def fetch_news():
    try:
        top_headlines = newsapi.get_top_headlines(language = 'en')

        headlines = [article['title'] for article in top_headlines['articles']]
        return headlines

    except Exception as e:
        print("Error fetching news:", e)
        return []

def fetch_weather(city_name):
    try:
        # API endpoint for current weather by city name
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        
        # Fetch weather data
        response = requests.get(url)
        data = response.json()
        
        # Extract relevant weather information
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        
        # Format weather update
        weather_update = f"The weather in {city_name} is currently {weather_description}. The temperature is {temperature} degrees Celsius."
        
        return weather_update
    except Exception as e:
        print("Error fetching weather:", e)
        return "Unable to fetch weather information."

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except Exception as e:
        print("Error:", e)
        return None

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

    #logic

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'rick roll me' in query:
            webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

        elif 'open google' in query:
            webbrowser("google.com")

        elif 'open kaggle' in query:
            webbrowser("https://www.kaggle.com/")

        elif 'play kanye' in query:
            music_dir = 'D:\\SHASHWAT\\Donda 2'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is,{strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\91982\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open apple music' in query:
            webbrowser.open("https://music.apple.com/in/home?l=en-GB")

        elif 'play frank ocean' in query:
            music_dir = "D:\\SHASHWAT\\frank ocean"
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir , random_song))

        elif 'play news' in query:
            
            news_headlines = fetch_news()
            if news_headlines:

                selected_headline = random.choice(news_headlines)

                engine = pyttsx3.init()
                engine.say(selected_headline)
                engine.runAndWait()
            else:
                print('No new headlines available.')
        

        elif 'weather' in query:
        # Check if city_name is provided in the query
            if 'city_name' in query:
                city_name = "New Delhi"  # Default city name if not provided
            else:
                # Prompt the user to input the city name
                city_name = input("Please enter the city name: ")
        
            weather_update = fetch_weather(city_name)
        
            # Speak the weather update
            engine = pyttsx3.init()
            engine.say(weather_update)
            engine.runAndWait()
        
        elif 'open x' in query:
            webbrowser("https://twitter.com/home")

        elif 'translate' in query:
            print("Speak the text you want to translate...")
            input_text = recognize_speech()
            if input_text:
                target_language = input("Enter the language code of the target language (e.g., 'fr' for French): ")
                translated_text = translate_text(input_text, target_language)
                print("Translated Text:", translated_text)
                speak(translated_text)





        elif 'quit' in query:
            exit()
