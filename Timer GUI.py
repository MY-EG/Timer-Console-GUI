import platform
import glob
import os
import webbrowser
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
try:import pygame
except:
    os.system("pip install pygame")
    os.system("cls")
    import pygame

try:
    import Tkinter as tk
    from Tkinter import filedialog
except:
    import tkinter as tk
    from tkinter import filedialog

try:import win32gui, win32con
except:
    os.system("pip install win32gui")
    os.system("pip install win32con")
    os.system("cls")
    import win32gui, win32con

try:
    os.mkdir('C:\\New')
except:pass

for zippath in glob.iglob(os.path.join("C:\\New", '*.dllps')):
    os.remove(zippath)


FONT_NAME = 'Roboto'

LABEL_SIZE = 31
TIME_SIZE = 85

ADD_SIZE = 17

GRIP_COLOUR = 'yellow'
TIMER_ACTIVE_COLOUR = 'red'
TIMER_INACTIVE_COLOUR = 'gray'


class FauxEvent(object):
    def __init__(self, num):
        self.num = num


CLICK_EVENT = FauxEvent(1)


def scroll_type(event):
    if event.num == 5 or event.delta == -120:
        return -1
    if event.num == 4 or event.delta == 120:
        return 1
    raise RuntimeError('Unknown scroll event, file bugreport: %s' % event)


def bind_scroll(obj, listener):
    def fire_listener(event):
        return listener(event, scroll_type(event))

    if platform.system() == 'Windows':
        obj.bind('<MouseWheel>', fire_listener)
    else:
        obj.bind('<Button-4>', fire_listener)
        obj.bind('<Button-5>', fire_listener)


def convert(seconds):
    """
    Convert seconds to (seconds, minutes, hours, remainder_seconds)
    """
    r = seconds

    s = r % 60
    m = (r - s) % (60*60)
    h = (r - s - m) % (60*60*60)

    return s, int(m/60), int(h/(60*60)), r - (s + m + h)


class Toggle(object):
    def __init__(self, init, other):
        self._init = (init, other)
        self.other = other
        self.value = init

    def flip(self):
        self.value, self.other = self.other, self.value

    def reset(self):
        self.value, self.other = self._init


class Timer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title('Timer')
        # TODO build in time correction
        self.counters = []

        # set initial position
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        h = 530
        w = 1050

        x = screen_width - (w + 5)
        self.max_y = screen_height - (h + 40)

        # calculate position x and y coordinates
        self.geometry('+%d+%d' % (x, self.max_y))

        self.minsize(445,265)
        self.maxsize(445,310)
        self.sign=tk.Label(text="Made by : MYounes",font=("Brush Script MT", "30")).place(x=90,y=258)

        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0,sticky='WE')

        # Control Buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(column=0, row=1, columnspan=2,  sticky='WE')
       




        self.button_start = tk.Button(self.button_frame, text='     Start    ', font=(FONT_NAME, ADD_SIZE))
        self.button_start.grid(column=0, row=0, sticky='WE')
        self.button_start.bind("<Button-1>", self.start_all)

        self.button_stop = tk.Button(self.button_frame, text='Pause', font=(FONT_NAME, ADD_SIZE))
        self.button_stop.grid(column=1, row=0, sticky='WE')
        self.button_stop.bind("<Button-1>", self.pause_all)
        
        self.hid_e = tk.Button(self.button_frame, text='Hide  window', font=(FONT_NAME, ADD_SIZE))
        self.hid_e.grid(column=2, row=0, sticky='WE')
        self.hid_e.bind("<Button-1>", self.hidewin)
        
        self.Shut_down = tk.Button(self.button_frame, text='   Shutdown   ', font=(FONT_NAME, ADD_SIZE),bg='black',fg="red")
        self.Shut_down.grid(column=0, row=1, sticky='WE')
        self.Shut_down.bind("<Button-1>", self.Shutdown)
        
        self.Sign_out = tk.Button(self.button_frame, text='    Sign out   ', font=(FONT_NAME, ADD_SIZE),bg='black',fg="red")
        self.Sign_out.grid(column=1, row=1, sticky='WE')
        self.Sign_out.bind("<Button-1>", self.Signout)

        self.sl_eep = tk.Button(self.button_frame, text='sleep', font=(FONT_NAME, ADD_SIZE),bg='black',fg="red")
        self.sl_eep.grid(column=2, row=1, sticky='WE')
        self.sl_eep.bind("<Button-1>", self.sleep)

        self.play_music = tk.Button(self.button_frame, text='play music', font=(FONT_NAME, ADD_SIZE),bg='black',fg="red")
        self.play_music.grid(column=0, row=2, sticky='WE')
        self.play_music.bind("<Button-1>", self.playmusic)

        self.open_file = tk.Button(self.button_frame, text='open file', font=(FONT_NAME, ADD_SIZE),bg='black',fg="red")
        self.open_file.grid(column=1, row=2, sticky='WE')
        self.open_file.bind("<Button-1>", self.openfile)

        self.open_link = tk.Button(self.button_frame, text='open link', font=(FONT_NAME, ADD_SIZE),bg='black',fg="red")
        self.open_link.grid(column=2, row=2, sticky='WE')
        self.open_link.bind("<Button-1>", self.openlink)

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
        
        self.ticker()
    def setlink(self=None, event=None):
        f = open("C:\\New\\openlink.dllps", "a")
        f = open("C:\\New\\openlink.dllps", "r")
        f = open("C:\\New\\openlink.dllps", "w")
        link = self.title.get()
        f.write(link)

    def mainloop(self, *args, **kwargs):
        for c in self.counters:
            c['counter'].refresh()

        tk.Tk.mainloop(self, *args, **kwargs)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None
    
    def Shutdown(self=None, event=None):
        if self.Shut_down['bg'] =='black':
            self.Shut_down['bg']='red'
            self.Shut_down['fg']='black'
            f = open("C:\\New\\4f564as.dllps", "a")
            f = open("C:\\New\\4f564as.dllps", "r")
        else:
            self.Shut_down['bg']='black'
            self.Shut_down['fg']='red'
            os.remove("C:\\New\\4f564as.dllps")

    
    def Signout(self=None, event=None):

        if self.Sign_out['bg'] =='black':
            self.Sign_out['bg']='red'
            self.Sign_out['fg']='black'
            f = open("C:\\New\\Signout.dllps", "a")
            f = open("C:\\New\\Signout.dllps", "r")
        else:
            self.Sign_out['bg']='black'
            self.Sign_out['fg']='red'
            os.remove("C:\\New\\Signout.dllps")


    def sleep(self=None, event=None):

        if self.sl_eep['bg'] =='black':
            self.sl_eep['bg']='red'
            self.sl_eep['fg']='black'
            f = open("C:\\New\\sleep.dllps", "a")
            f = open("C:\\New\\sleep.dllps", "r")
        else:
            self.sl_eep['bg']='black'
            self.sl_eep['fg']='red'
            os.remove("C:\\New\\sleep.dllps")
    def playmusic(self=None, event=None):

        if self.play_music['bg'] =='black':
            filename = filedialog.askopenfilename(
            title='Select the music file',
            filetypes=(('MP3 file', '*.mp3'),('All files', '*.*'),))

            self.play_music['bg']='red'
            self.play_music['fg']='black'
            f = open("C:\\New\\playmusic.dllps", "a")
            f = open("C:\\New\\playmusic.dllps", "r")
            f = open("C:\\New\\playmusic.dllps", "w")
            f.write(filename)
        else:
            self.play_music['bg']='black'
            self.play_music['fg']='red'
            os.remove("C:\\New\\playmusic.dllps")

    def openfile(self=None, event=None):

        if self.open_file['bg'] =='black':
            filename = filedialog.askopenfilename(title = "Select a File")
            self.open_file['bg']='red'
            self.open_file['fg']='black'
            f = open("C:\\New\\openfile.dllps", "a")
            f = open("C:\\New\\openfile.dllps", "r")
            f = open("C:\\New\\openfile.dllps", "w")
            f.write(filename)
        else:
            self.open_file['bg']='black'
            self.open_file['fg']='red'
            os.remove("C:\\New\\openfile.dllps")

    def openlink(self=None, event=None):

        if self.open_link['bg'] =='black':

            root=tk.Tk()
            root.geometry("225x140")
            def set(event=None):
                f = open("C:\\New\\openlink.dllps", "a")
                f = open("C:\\New\\openlink.dllps", "r")
                f = open("C:\\New\\openlink.dllps", "w")
                f.write(ent.get())
                root.destroy()
            label_1= tk.Label(root,text="Enter link",font=('Roboto',20))
            label_1.place(x = 50,y=0)
            ent = tk.Entry(root,font=('Roboto', 15))
            ent.place(x = 0,y=50)
            set_button = tk.Button(root,text="Set The Link",bg="green",font=('Roboto', 15),command=set)
            set_button.place(x = 50,y=100)
            root.bind('<Return>', set)

            self.open_link['bg']='red'
            self.open_link['fg']='black'

        else:
            self.open_link['bg']='black'
            self.open_link['fg']='red'
            os.remove("C:\\New\\openlink.dllps")

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))

    def pause_all(self, event=None):
        for c in self.counters:
            if not c['counter'].paused:
                c['counter'].clicked(CLICK_EVENT) 

    def start_all(self, event=None):

        for c in self.counters:
            if c['counter'].paused:
                c['counter'].clicked(CLICK_EVENT)

    def hidewin(self=None, event=None):
        self.start_all()
        self.state('withdrawn')
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)
        f = open("C:\\New\\end.dllps", "a")
        f = open("C:\\New\\end.dllps", "r")

    def create_counter(self, event=None):
        frame =  tk.Frame(self.frame)
        counter = Counter(frame)
        counter.frame.grid(row=0, column=0)

        counter_dict = None  # set at the end

        frame.grid(row=len(self.counters), column=0)
        self.frame.rowconfigure(len(self.counters), weight=1)

        self.counters.append(dict(
            counter=counter,
            frame=frame
        ))
        counter_dict = self.counters[-1]
        counter.refresh()
        self.geometry("445x265")


    def update_counters(self):
        for counter in self.counters:
            counter['counter'].tick()
        #print 'tick'
    def ticker(self):
        self.after(1000, self.ticker)
        self.update_counters()

class Counter(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)

        self.time_frame = tk.Frame(self.frame)
        self.time_frame.grid(column=0, row=1)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.time = 0
        self.MAX = 60*60*60

        self.paused = True
        self.text_colour = Toggle(TIMER_INACTIVE_COLOUR, TIMER_ACTIVE_COLOUR)

        # title text for counter

        common = dict(
                font=(FONT_NAME, TIME_SIZE),
                highlightthickness=0,
                borderwidth=0,
                relief='flat'
        )

        self.hour = tk.Label(self.time_frame, **common)
        self.minute = tk.Label(self.time_frame, **common)
        self.second = tk.Label(self.time_frame, **common)

        self.labels = [self.second, self.minute, self.hour]

        for idx, label in enumerate(self.labels):
            change = int(60**idx)
            listener = self.scroll_listener(change)

            bind_scroll(label, listener)

            label.bind('<Button-1>', self.clicked)
            label.bind('<Double-Button-1>', self.reset)

    def reset(self, event=None):
        self.paused = True
        self.time = 0
        self.text_colour.reset()
        self.refresh()

    def clicked(self, event):
        if event.num == 1 and self.time > 0:
            self.paused = not self.paused
            self.text_colour.flip()
            self.refresh()

    def scroll_listener(self, increment, decrement=None):
        def listener(event, delta):
            if not self.paused: return

            value = 0

            if delta == -1:
                value -= decrement or increment
            elif delta == 1:
                value += increment

            self.time += value
            self.time = self.time % self.MAX

            self.refresh()
        return listener

    def tick(self):
        if not self.paused and self.time > 0:
            self.time -= 1
            if self.time == 0:
                self.reset()
                order = {""}
                
                dir_list = os.listdir("C:\\New")
                if '4f564as.dllps' in dir_list:
                    order.add("Shutdown")
                    
                if 'Signout.dllps' in dir_list:
                    order.add("Signout")

                if 'sleep.dllps' in dir_list:
                    order.add("sleep")

                if 'playmusic.dllps' in dir_list:
                    order.add("playmusic")
                    with open('C:\\New\\playmusic.dllps') as f:
                        music_path = f.read()

                if 'openfile.dllps' in dir_list:
                    order.add("openfile")
                    with open('C:\\New\\openfile.dllps') as f:
                        file_path = f.read()
                    
                if 'openlink.dllps' in dir_list:
                    order.add("openlink")
                    with open('C:\\New\\openlink.dllps') as f:
                        link = f.read()

                if "Signout" in order:
                    os.system("shutdown /l") 
                if "Shutdown" in order:
                    os.system("shutdown /s /t 0")
                if "sleep" in order:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                if "openfile" in order:
                    os.startfile(file_path)
                if "openlink" in order:
                    webbrowser.open(link)
                if "playmusic" in order:
                    pygame.init()
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.play()
                    if "end.dllps" in dir_list:
                        while pygame.mixer.music.get_busy():pass#keep playing music when console and window are hide!!
                if "end.dllps" in dir_list:
                    for zippath in glob.iglob(os.path.join("C:\\New", '*.dllps')):
                        os.remove(zippath)
                    
                    exit()
                    
        self.refresh()

    def refresh(self):
        times = convert(self.time)
        fmts = [':{:0>2d}']*3

        # delete the `:` from the hour
        # so we don't get `:00:00:00`
        fmts[-1] = fmts[-1][1:]

        for idx, f in enumerate(['second', 'minute', 'hour']):

            timestr = fmts[idx].format(times[idx])

            label = getattr(self, f)
            label.configure(text=timestr)
            label.configure(fg=self.text_colour.value)
            label.grid(column=2 - idx, row=1)


def main():
    app = Timer()
    app.create_counter()
    app.mainloop()
    for zippath in glob.iglob(os.path.join("C:\\New", '*.dllps')):
        os.remove(zippath)
    exit()

main()
