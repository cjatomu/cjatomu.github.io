#one
import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
print("========================================")
print("Welcome to the TV Listings Program")
print("Today's date:",datetime.strftime("%x"))
print("Current time:",datetime.strftime("%X"))
print("========================================")
program = programs[0]
time = times[0]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
# Next show
print("========================================")
print("Welcome to the TV Listings Program")
print("Today's date:",datetime.strftime("%x"))
print("Current time:",datetime.strftime("%X"))
print("========================================")
program = programs[1]
time = times[1]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
# Next show
print("========================================")
print("Welcome to the TV Listings Program")
print("Today's date:",datetime.strftime("%x"))
print("Current time:",datetime.strftime("%X"))
print("========================================")
program = programs[2]
time = times[2]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
# Next show
print("========================================")
print("Welcome to the TV Listings Program")
print("Today's date:",datetime.strftime("%x"))
print("Current time:",datetime.strftime("%X"))
print("========================================")
program = programs[3]
time = times[3]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
# Finish
print("========================================")
print("Welcome to the TV Listings Program")
print("Today's date:",datetime.strftime("%x"))
print("Current time:",datetime.strftime("%X"))
print("========================================")
input("Press enter to close this program")


#Two
import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
def displaytime():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")
displaytime()
program = programs[0]
time = times[0]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
displaytime()
program = programs[1]
time = times[1]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
displaytime()
program = programs[2]
time = times[2]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
displaytime()
program = programs[3]
time = times[3]
print()
print(program,"is on tomorrow at",time)
print("Press 'Enter' to get the next program")
input()
print()
displaytime()
input("Press enter to close this program")


#Three
import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
def displaytime():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")
displaytime()
program = programs[0]
time = times[0]
def displayprogram():
    print()
    print(program,"is on tomorrow at",time)
    print("Press 'Enter' to get the next program")
    input()
    print()
displayprogram()
displaytime()
program = programs[1]
time = times[1]
displayprogram()
displaytime()
program = programs[2]
time = times[2]
displayprogram()
displaytime()
program = programs[3]
time = times[3]
displayprogram()
displaytime()
input("Press enter to close this program")


#Four
import time as datetime
programs = ["Coronation Street","Eastenders","Emmerdale","Hollyoaks"]
times = ["20:00","19:30","19:00","18:30"]
def displaytime():
    print("========================================")
    print("Welcome to the TV Listings Program")
    print("Today's date:",datetime.strftime("%x"))
    print("Current time:",datetime.strftime("%X"))
    print("========================================")
displaytime()
program = programs[0]
time = times[0]
def displayprogram():
    print()
    print(program,"is on tomorrow at",time)
    print("Press 'Enter' to get the next program")
    input()
    print()
num=int(1)
while num!=int(4):
    displayprogram()
    displaytime()
    program = programs[num]
    time = times[num]
    num=num+1
input("Press enter to close this program")
