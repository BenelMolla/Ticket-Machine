import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        time_sec -= 1

    print("time out")

def perfumery():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + 1, b + 1

    Ticket = perfumery()
    while True:
        customer = input("choose p for perfumery ")
        if customer == "c":
            print(next(Ticket))


perfume = perfumery()


def Pharmaceuticals():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + 1, b + 1

    z = Pharmaceuticals()
    while True:
        customer = input("choose ph for Pharmaceuticals ")
        if customer == "c":
            print(next(z))


pharmacy = Pharmaceuticals()


def cosmotics():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + 1, b + 1

    z = cosmotics()
    while True:
        customer = input("choose c for cosmetics ")
        if customer == "c":
            print(next(z))


cosmo = cosmotics()
def main_data():
    place = int(input("choose your option: "))
    if place == 1:
        print("\n\t\t\t\t reservation")
        print("\t\t\t\tyour ticket number is:", "ph", next(perfume))
        print("""\t\t\t\tNow Take your ticket! thanks:
                                Date: 1 November 2022
                                Start time: \t20:21
                                End time: \t22:21\n
                                """)
        print("\n")
    elif place == 2:
        print("\n\t\t\t\t reservation")
        print("\t\t\t\tyour ticket number is:", "ph", next(pharmacy))
        print("""\t\t\t\tNow Take your ticket! thanks:
                        Date: 1 November 2022
                        Start time: \t20:21
                        End time: \t22:21\n
                        """)
        print("\n")

    elif place == 3:
        print("\n\t\t\t\t reservation")
        print("\t\t\t\tyour ticket number is:", "ph", next(cosmo))
        print("""\t\t\t\tNow Take your ticket! thanks:
                                Date: 1 November 2022
                                Start time: \t20:21
                                End time: \t22:21\n
                                """)
        print("\n")




    else:
        print("wrong choice")

    duud()
def duud():
    print("Hi welcome to our drug store: ")
    print("where you want to go:")
    print("\t1, perfumery")
    print("\t2, Pharmaceuticals")
    print("\t3, Cosmetics")
    ID = [346549306, 346369432]
    count = 0
    user = int(input("please enter your id:   "))
    while count < 2:
        if user in ID:
            print("\t\t\t\t\t\tyou are registered, welcome and select your destination")
            main_data()
        else:
            print("\t\t\t\t\t\tyou are not rigistered, sorry")
            user = int(input("please enter your id:   "))
            count += 1
    else:
        print("\t\t\t\t\t\tyou are now BLOCKED for 5 sec, sorry")
        print("sorry u have to stay for 5 sec to try again")
        countdown(int(5))
duud()


