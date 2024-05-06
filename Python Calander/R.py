import CR
import L
import CD
import OL
import L
import test
import time
import CR


def full():
    monday = open('monday.txt', 'r')
    tuesday = open('tuesday.txt', 'r')
    wednesday = open('wednesday.txt', 'r')
    thursday = open('thursday.txt', 'r')
    friday = open('friday.txt', 'r')
    saturday = open('saturday.txt', 'r')
    sunday = open('sunday.txt', 'r')

    printe = ["Monday: " + monday.read(),
              "Tuesday: " + tuesday.read(),
              "Wednesday: " + wednesday.read(),
              "Thursday: " + thursday.read(),
              "Friday: " + friday.read(),
              "Saturday" + saturday.read(),
              "Sunday" + sunday.read()]

    for x in printe:
        time.sleep(0.21)
        print(CR.TextColors.end + x)


day = int


def submission():
    global day
    print("\n" * 100)
    for j in OL.week:
        print(CR.TextColors.end + "-" * 9 + CR.TextColors.end + j)
    day = int(input("-" * 9 + CR.TextColors.cyan + "What day:  "))
    text()


def use():
    i = input("what do you want to add on monday")
    for d in L.Monday:
        print(d)


def text():
    global day
    if day == 0:
        L.monday()
    elif day == 1:
        L.tuesday()
    elif day == 2:
        L.wednesday()
    elif day == 3:
        L.thursday()
    elif day == 4:
        L.friday()
    elif day == 5:
        L.saturday()
    else:
        L.sunday()
