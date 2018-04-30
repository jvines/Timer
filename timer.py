from Tkinter import *
import time

class Timer:
    def __init__(self,hr,mn,sc):

        self.delay = sc + (mn + 60*hr)*60

        self.start = time.time()
        self.pausetime = 0.00
        self.timeatpause = self.start
        self.actual_time = self.delay
        self.ispause = True

    ### Updates the time in the timer
    def update(self):

        if self.ispause==False:
            self.actual_time = time.time() - self.start + self.delay

        if self.ispause==True:
            self.actual_time = self.timeatpause - self.start + self.delay

    ### Pauses the Timer
    def pause(self):
        self.ispause = True
        self.timeatpause = time.time()

    ### Unpauses the Timer
    def unpause(self):
        self.ispause = False
        self.pausetime = time.time() - self.timeatpause
        self.start += self.pausetime


    ### Returns the time elapsed in HH:mm:ss.
    def get_time_hhmmss(self):
        end = self.actual_time
        m, s = divmod(end, 60)
        h, m = divmod(m, 60)
        time_str = "%02d:%02d:%02d" % (h, m, s)
        return time_str



## Input starting time

hr = int(input('Initial Hours: '))
mn = int(input('Initial Minutes: '))
sc = int(input('Initial Seconds: '))

#Create a timer
timer = Timer(hr,mn,sc)


#Create a window
root = Tk()
T = Text(root)
T.pack()
T.insert(END, "Time")
mainloop()

#Print start time
print timer.get_time_hhmmss()

while True:

    #Command input: #0 print, #1 pause/unpause
    x = int(input('Enter Command: '))
    timer.update() #We update the timer

    if x==0:
        print timer.get_time_hhmmss()

    elif x==1:
        if timer.ispause==True:
            timer.unpause()
        else:
            timer.pause()
