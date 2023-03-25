import Mini_Voice_Assistant as mva

def questions(str):
    s=str.lower()
    if(s=="what is your name"):
        return 'my name is junior ramsh'
    elif(s=="EXIT"):
        mva.speak("Okay sir thank You")
    else:
        return "oooops i've to search that in google"





