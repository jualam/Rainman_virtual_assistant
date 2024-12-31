#pip install speechrecognition pyaudio
#pip install pyttsx3
#pip install setuptools
#pip install webbrowser
#pip install pocketsphinx
#pip install openai
#pip install gTTS
#pip install pygame(to play the mp3)

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

engine = pyttsx3.init()
newsapi="NEWS_API"

#using pyttsx3
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

#using gTTS
def speak_new(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client=OpenAI(api_key="OPEN_AI_API")
    # Create the chat completion request
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assitant named RainMan skilled in regular question answering tasks for everyday works. Please give short responses maximum 100 words"},
            {"role": "user", "content": command}
        ]
    )
    # return the response message
    return (completion.choices[0].message.content)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak_old(article['title'])
    else:
        output= aiProcess(c)
        speak_old(output)
        
if __name__ == "__main__":
    speak_old("Initializing Rainman....")
    while True:
        # Listen for the wake word "Rainman"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(f"Heard: {word}") #debugging step
            if word.replace(" ", "").lower() == "rainman":
                speak_old("Yeah")
                # Listen for command
                with sr.Microphone() as source:
                    print("RainMan Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
            elif(word.lower()=="stop"):
                break


        except Exception as e:
            print("Error; {0}".format(e))
