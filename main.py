import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary

recignizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

    if c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f'Playing {song}')
            webbrowser.open(link)
        else:
            speak("Sorry i cant find that song in my library")

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