file = open('monday.txt', 'r')
m = file.read()


def tuesday():
    fileTwo = open('monday.txt', 'a')
    file = open('monday.txt', 'r')
    fileTwo.write(input("input:  "))
    file.read()
