import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
import requests
import openai as OpenAI
from gtts import gTTS
import pygame

recignizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "65caba6136d34a2d98121055b0808fb2"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("hello.mp3")

    pygame.mixer.init()
    pygame.mixer.music.unload()
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def aiProcess(command):
    client = OpenAI(
    api_key="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",
)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant named kaizen, consisting general task like alexa. GIve short responces",
            },
            {
                "role": "user",
                "content": command,
            },
        ],
    )

    return completion.choices[0].message.content

def processcommand(c):
    if "open" in c.lower():
        if "youtube" in c.lower():
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")
        elif "google" in c.lower():
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "github" in c.lower():
            speak("Opening Github")
            webbrowser.open("https://www.github.com")
        elif "notepad" in c.lower():
            speak("Opening Notepad")
            webbrowser.open("notepad.exe")
        else:
            speak("Sorry, I cannot open that.")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f'Playing {song}')
            webbrowser.open(link)
        else:
            speak("Sorry i cant find that song in my library")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json() #parse the json response
            articles = data.get('articles', []) #get the articles from response
            for article in articles:
                speak(article['title'])

    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Kaizen...")
    while True:
        r = sr.Recognizer()
            # recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print(word)
            if word.lower() =="kaizen":
                speak("Yes Boss!")
                with sr.Microphone() as source:
                    print("Kaizen activated...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processcommand(command)
                           
        except Exception as e:
            print("Error occured; {0}".format(e))