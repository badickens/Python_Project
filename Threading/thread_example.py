#! python3


from threading import Thread
import time

def timer(name, delay, repeat):
    print("Timer:" + name + " Started\n")
    while repeat > 0:
        time.sleep(delay)
        print('\n' + name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + " Completed")

def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 1, 5))
    t1.start()
    t2.start()

    print("Main Complete\n")

if __name__ == '__main__':
    Main()
                                
'''
sample of output

Timer:Timer1 Started

Main Complete

Timer:Timer2 Started
>>> 

Timer1: Fri Sep  4 16:48:05 2015

Timer2: Fri Sep  4 16:48:05 2015

Timer1: Fri Sep  4 16:48:06 2015

Timer2: Fri Sep  4 16:48:06 2015

Timer1: Fri Sep  4 16:48:07 2015

Timer2: Fri Sep  4 16:48:07 2015

Timer1: Fri Sep  4 16:48:08 2015

Timer2: Fri Sep  4 16:48:08 2015

Timer1: Fri Sep  4 16:48:09 2015
Timer: Timer1 Completed

Timer2: Fri Sep  4 16:48:09 2015
Timer: Timer2 Completed

'''
