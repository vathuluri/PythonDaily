import datetime
now = datetime.datetime.now()

name = raw_input("What is your name?: ")
age = int(input("How old are you: "))
year = str((now.year - age)+100)
print(name + " will be 100 years old in the year " + year)