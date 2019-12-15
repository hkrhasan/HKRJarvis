import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning HKR!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon HKR!")
    else:
        speak("Good Evening HKR!")

    speak("I am your goolaaam Sir. Please tell me how may i help you")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    
    # Speech recognition using Google Speech Recognition
    try:
        print("Recognizing...")
        r.pause_threshold = 1
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        query = r.recognize_google(audio)
        print("User said: "+query+"\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("yourEmail@gmail.com",'your_pass')
    server.sendmail('yourEmail@gmail.com', to, content)
    server.close()




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open github" in query:
            webbrowser.open("github.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = 'your music folder path'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is "+strTime)
        elif "open sublime" in query:
            subl_path = "C:\\Program Files (x86)\\Sublime Text 3\\sublime_text.exe"
            os.startfile(subl_path)
        elif "email to talib" in query:
            try:
                speak("what shoul i say!!")
                content = takeCommand()
                to = "example@gmail.com"
                sendMail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("sorry HKR , I am not able to send this email..")
