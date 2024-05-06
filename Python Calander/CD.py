from datetime import datetime
from datetime import date
import CD

today = date.today()
week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
dateWeek = str(week[datetime.weekday(today)])
date = datetime.weekday(CD.today)
