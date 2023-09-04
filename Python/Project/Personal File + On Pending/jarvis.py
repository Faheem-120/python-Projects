import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis A.I. Please tell me Faheem sir how may i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        
        elif 'open python' in query:
            webbrowser.open("python.org")
        
        elif 'open wordpress' in query:
            webbrowser.open("wordpress.com")

        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")
        
        elif 'open porn' in query:
            webbrowser.open("pornhub.com")

        elif 'open movies' in query:
            webbrowser.open("katmovies.hd")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open tailwind css' in query:
            webbrowser.open("tailwindcss.com")
        
        elif 'open aiou' in query:
            webbrowser.open("aiou.com")
        
        elif 'open iub' in query:
            webbrowser.open("iub.com")
        
        elif 'open paypal' in query:
            webbrowser.open("paypal.com")
        
        elif 'open jazzcash' in query:
            webbrowser.open("jazzcash.com")

        elif 'tell me about weather' in query:
            webbrowser.open("weather.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play the music' in query:
            music_dir = 'D:\\Audio Songs\\friday.mp3'
            songs = os.listdir(music_dir)
            print("Playing your song" , songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'Tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Faheem Qasim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to faheem' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "muneebqasim786308@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir Faheem Qasim. I am not able to send this email")
        else:
            print("No query matched")

        
