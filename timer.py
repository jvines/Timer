import time
from Tkinter import *


class Timer:
    def __init__(self, hr=0, mn=0, sc=0):

        self.hr = hr
        self.mn = mn
        self.sc = sc

        self.delay = self.sc + (self.mn + 60 * self.hr) * 60

        self.start_time = time.time()
        self.pause_time = 0.00
        self.time_at_pause = self.start_time
        self.actual_time = self.delay
        self.pause = True

    ########################### GETTERS AND SETTERS ###########################

    def set_delay(self):
        self.delay = self.sc + (self.mn + 60 * self.hr) * 60
        self.actual_time = self.delay
        pass

    def set_hr(self, hr):
        self.hr = hr
        pass

    def set_mn(self, mn):
        self.mn = mn
        pass

    def set_sc(self, sc):
        self.sc = sc
        pass

    def set_time(self, hr, mn, sc):
        self.set_hr(hr)
        self.set_mn(mn)
        self.set_sc(sc)
        self.set_delay()
        pass

    def set_pause(self):
        self.pause = True
        pass

    def set_unpause(self):
        self.pause = False
        pass

    def get_hr(self):
        return self.hr

    def get_mn(self):
        return self.mn

    def get_sc(self):
        return self.sc

    def is_paused(self):
        return self.pause

    ###########################################################################

    # Updates the time in the timer
    def update(self):
        if not self.pause:
            self.actual_time = time.time() - self.start_time + self.delay

        if self.pause:
            self.actual_time = self.time_at_pause - self.start_time + self.delay
            pass

    # Pauses the Timer
    def stop(self):
        self.set_pause()
        self.time_at_pause = time.time()
        pass

    # Unpauses the Timer
    def start(self):
        self.set_unpause()
        self.pause_time = time.time() - self.time_at_pause
        self.start_time += self.pause_time
        pass

    # Returns the time elapsed in HH:mm:ss.
    def get_time_hhmmss(self):
        end = self.actual_time
        m, s = divmod(end, 60)
        h, m = divmod(m, 60)
        time_str = "%02d:%02d:%02d" % (h, m, s)
        return time_str


# Input starting time


# hr = int(input('Initial Hours: '))
# mn = int(input('Initial Minutes: '))
# sc = int(input('Initial Seconds: '))

# Create a timer
# timer = Timer(hr, mn, sc)
#
#
# # Create a window
# root = Tk()
# T = Text(root)
# T.pack()
# T.insert(END, "Time")
# mainloop()

# Print start time
# print timer.get_time_hhmmss()
#
# while True:
#
#     # Command input: #0 print, #1 pause/unpause
#     x = int(input('Enter Command: '))
#     timer.update()  # We update the timer
#
#     if x == 0:
#         print timer.get_time_hhmmss()
#
#     elif x == 1:
#         if timer.ispause == True:
#             timer.unpause()
#         else:
#             timer.pause()
