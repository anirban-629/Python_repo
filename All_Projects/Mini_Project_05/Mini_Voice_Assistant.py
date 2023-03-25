from win32com.client import Dispatch
import speech_recognition as sr
import greet as gr
import questions as q


def speak(str):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)


def input_exception():
    str = "sorry sir I couldn't recognize your voice"
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)


def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        ans = q.questions(text)
        speak(ans)
    except Exception as e:
        input_exception()


if __name__ == '__main__':
    speak(f"{gr.greet()} sir I'm a Baby assistant made by you..!")
    speak("how can i Help you")
    print("Speak..!!")
    input()
