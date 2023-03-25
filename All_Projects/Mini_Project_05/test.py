from win32com.client import Dispatch
import webbrowser
import speech_recognition as sr

def speak(str):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)

def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        url=f"https://www.{text}.com"
        webbrowser.open(url)
    except Exception:
        speak("Couldn't Recognize your voice sir... Please try again.!!")
        speak("Tell me Any website...I'll Open it for you")
        input()

speak("Tell me Any website...I'll Open it for you")
input()

