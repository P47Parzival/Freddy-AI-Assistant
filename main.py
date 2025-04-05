import speech_recognition as sr
import webbrowser
import pyttsx3 

recignizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")


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