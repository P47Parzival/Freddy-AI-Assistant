import speech_recognition as sr
import webbrowser
import pyttsx3 

recignizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand():
    pass

if __name__ == "__main__":
    speak("Initializing Kaizen...")
    while True:
        r = sr.Recognizer()
            # recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
            word = r.recognize_google(audio)
            print(word)
            if word.lower() =="kaizen":
                speak("Yes Boss!")
                with sr.Microphone() as source:
                    print("Kaizen activated...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=10)
                    command = r.recognize_google(audio)

                    processcommand()
                           
        except Exception as e:
            print("Error occured; {0}".format(e))