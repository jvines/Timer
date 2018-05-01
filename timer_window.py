import tkFont
import Tkinter as tk
import tkMessageBox
import ttk

from timer import *


class App(object):
    def __init__(self, master):
        self.master = master
        self.__create_selection_widgets__()
        self.timer = Timer()

    def __create_selection_widgets__(self):

        self.master.title('Timer')  # Window title
        h = StringVar()
        m = StringVar()
        s = StringVar()

        ############################### LABELS ################################
        self.hr_l = ttk.Label(self.master, text='Hr:')
        self.mn_l = ttk.Label(self.master, text='Min:')
        self.sc_l = ttk.Label(self.master, text='Seg:')

        self.hr_l.grid(row=0, column=0, sticky=E)
        self.mn_l.grid(row=0, column=2, sticky=E)
        self.sc_l.grid(row=0, column=4, sticky=E)
        #######################################################################

        ############################### ENTRIES ###############################
        self.hr = ttk.Entry(self.master, textvariable=h)
        self.mn = ttk.Entry(self.master, textvariable=m)
        self.sc = ttk.Entry(self.master, textvariable=s)

        self.hr.config(width=2)
        self.mn.config(width=2)
        self.sc.config(width=2)

        self.hr.insert(0, 0)
        self.mn.insert(0, 0)
        self.sc.insert(0, 0)

        self.hr.grid(row=0, column=1)
        self.mn.grid(row=0, column=3)
        self.sc.grid(row=0, column=5)
        #######################################################################

        ############################### BUTTONS ###############################
        b1_text = 'Set initial time'
        b2_text = 'Start from 0'
        b1 = ttk.Button(self.master, text=b1_text, command=self.set_time)
        b2 = ttk.Button(self.master, text=b2_text, command=self.fresh_start)

        b1.grid(row=1, column=0, columnspan=2)
        b2.grid(row=1, column=4, columnspan=2)
        #######################################################################

        def character_limit(*args):
            """Limits the entries characters to two values only."""
            var = args[0]
            if not var.get():
                var.set(0)
            if len(var.get()) > 2:
                var.set(var.get()[:2])

        # LISTENERS : They check the entry values!
        h.trace('w', lambda *args: character_limit(h))
        m.trace('w', lambda *args: character_limit(m))
        s.trace('w', lambda *args: character_limit(s))
        pass

    def destroy_window(self):
        slaves = self.master.grid_slaves()
        for s in slaves:
            s.destroy()
        pass

    def create_timer_window(self):
        init_time = self.timer.get_time_hhmmss()
        font = tkFont.Font(size=100)  # Controls font size
        self.timer_l = ttk.Label(self.master, text=init_time, font=font)
        self.b = ttk.Button(self.master, text='Start',
                            command=self.start_timer)
        save = ttk.Button(self.master, text='Save time', command=self.save_t)

        self.timer_l.grid(row=0, column=0, columnspan=3)
        self.b.grid(row=1, column=0)
        save.grid(row=1, column=2)
        pass

    def update_timer(self):
        self.timer_l['text'] = self.timer.get_time_hhmmss()
        self.loop()
        pass

    def loop(self):
        self.timer.update()
        self.master.after(1, self.update_timer)
        pass

    def after_button_refresh(self):
        self.destroy_window()
        self.create_timer_window()

    def set_time(self):
        h = int(self.hr.get())
        m = int(self.mn.get())
        s = int(self.sc.get())
        self.timer.set_time(h, m, s)
        self.after_button_refresh()
        pass

    def fresh_start(self):
        self.timer.set_time(0, 0, 0)
        self.after_button_refresh()
        pass

    def start_timer(self):
        if self.timer.is_paused():
            self.timer.start()
            self.b['text'] = 'Pause'
            self.b['command'] = self.pause_timer
        self.loop()
        pass

    def pause_timer(self):
        if not self.timer.is_paused():
            self.timer.stop()
            self.b['text'] = 'Start'
            self.b['command'] = self.start_timer
        pass

    def save_t(self):
        if not self.timer.is_paused():
            tkMessageBox.showerror('Error', 'Please pause the timer first')
            return

        F = open('time.dat', 'w')
        F.write(self.timer.get_time_hhmmss())
        F.close()
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
