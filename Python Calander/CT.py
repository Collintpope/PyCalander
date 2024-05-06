from datetime import datetime

currentTime = int
now = datetime.now()
current_time = int(now.strftime("%H"))
if current_time < 12:
    currentTime = "Good morning"
elif not 12 <= current_time >= 17:
    currentTime = "Good afternoon"
else:
    currentTime = "Good evening"
