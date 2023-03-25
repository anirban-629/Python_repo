from datetime import datetime

def greet():
    now = datetime.now()
    current_time_hour=now.strftime("%H")
    current_time_minute=now.strftime("%M")
    t1=int(current_time_hour)
    t2=int(current_time_minute)/100
    hour_min=t1+t2
    if(hour_min>=5.00 and hour_min<12.00):
        greetings="Good Morning"
        return greetings
    elif(hour_min>=5.00 and hour_min<12.00):
        greetings="Good Afternoon"
        return greetings
    else:
        greetings="Good Evening"
        return greetings
