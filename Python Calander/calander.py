import getpass
import readline
from datetime import datetime
import time
import CT
import CD
import OL
import CR
import R
import L
import test
import C

print(" " * 9 + CT.currentTime + " " + getpass.getuser().capitalize())
time.sleep(0.21)
print(" " * 9 + "Today is " + CD.dateWeek + " " + CR.TextColors.cyan + OL.emoitcons[CD.date])
time.sleep(0.21)
print(" " * 9 + CR.TextColors.red + OL.weekTwo[CD.date] + OL.TODO[CD.date])
submission = input("")
if submission == "add":
    R.submission()


elif submission == "full":
    R.full()
    if CD.date == 6 and CT.currentTime <= 18:
        open('sunday.txt', 'w').truncate(0)
        open('monday.txt', 'w').truncate(0)
        open('tuesday.txt', 'w').truncate(0)
        open('wednesday.txt', 'w').truncate(0)
        open('thursday.txt', 'w').truncate(0)
        open('friday.txt', 'w').truncate(0)
        open('saturday.txt', 'w').truncate(0)
    submission = input("")
    if submission == "add":
        R.submission()
