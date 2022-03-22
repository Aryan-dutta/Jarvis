import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()  # takes microphone input and returns string output
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login("youremail@gmail.com", "your-password")
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()  # Logic for executing tasks based on query
        if "wikipedia" or 'who is' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' or 'play youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif'email to aryan' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "yourEmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend Aryan bhai. I am not able to send this email")

        elif 'stop' in query:
            break
