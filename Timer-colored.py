from os import environ,system,startfile            # importing environ , system and startfil modules from the datetime library
from time import sleep                             # importing the timedelta module from the datetime library 
from datetime import timedelta                     # importing the timedelta module from the datetime library 

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'        # hiding pygame support sign
try:import pygame                                  # trying import pygame module
except:
    system("pip install pygame")
    system("cls")
    import pygame

import cpr                                         # importing cpr module to make colorful text on console
from webbrowser import open                        # importing the open module from the webbrowser library
try:from plyer import notification                 # trying import notification module from plyer library
except:
    system("pip install plyer")
    system("cls")
    from plyer import notification
from tkinter import filedialog                     # trying import filedialog module from tkinter library
try:import win32gui, win32con                      # trying import win32gui and win32con module
except:
    system("pip install win32gui")
    system("pip install win32con")
    system("cls")
    import win32gui, win32con


# defining the function to clean the console
clear = lambda: system("cls")    
clear()



# define the countdown function
def countdown(h, m, s):
	
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1

    # minutes and seconds format code ----------------

if __name__=="__main__":

    cpr.printgreen("Enter the time in hours: ")
    cpr.resetcolor()
    h = str(input())

    if h == '' :h = 0

    else :h = int(h)


    cpr.printgreen("Enter the time in minutes : ")
    cpr.resetcolor()
    m = str(input())

    if m == '' :m = 0

    else :m = int(m)

    cpr.printgreen("Enter the time in seconds: ")
    cpr.resetcolor()
    s =  str(input())

    if s == '' :s = 0

    else :s = int(s)


    # cleaning the screen ...
    clear()
    
    
    #                                  =================== chos from the list ===================

    cpr.printwhite("""
0 -  Nothing

1 -  Shutdown The PC

2 -  Restart The PC

3 -  Sleep

4 -  Send a notification

5 -  Sign out from the PC

6 -  play musuc

7 -  Open file

8 -  Open link in browser

9 -  Run CMD command

    """)

    cpr.printgreen("Choose a number to Do it when the time finish :")
    cpr.resetcolor()
    chos = input()

    # cleaning the screen ...
    clear()

    chos=" "+chos+" "

    max=9
    for i in range(1,max+1):
        if " "+str(i)+" " in chos:
            break
        if i==max:chos='00'
        

    if ' 4 ' in chos:

        cpr.printblue("Please enter the notification name :")
        cpr.resetcolor()
        notnam = input()

        cpr.printblue("\nEnter the notification message :")
        cpr.resetcolor()
        masg = input()

        cpr.printblue("\nSelect the notification icon :")
        cpr.resetcolor()
        filesname = 'icon files'
        filetype = 'ico'
        ourtitel = 'Select the notification icon'
        filetypes = (
        ('Icon file', '*.ico'),
        ('All files', '*.*'),
        )
        iconn = filedialog.askopenfilename(
        title='Select the notification icon',
        filetypes=filetypes,
        )
        # cleaning the screen ...
        clear()
        if notnam == '':notnam = ' '
        
        if masg == '':masg = ' '
        
        # cleaning the screen ...
        clear()

    if ' 9 ' in chos:

        cpr.printblue("Please enter the command :")
        cpr.resetcolor()
        comm = input()
        # cleaning the screen ...
        clear()

    if ' 6 ' in chos:

        cpr.printblue("Select music :")
        cpr.resetcolor()
        filetypes = (
            ('MP3 file', '*.mp3'),
            ('All files', '*.*'),
        )
        orr = filedialog.askopenfilename(
            title='Select the music file',
            filetypes=filetypes,
        )
        # cleaning the screen ...
        clear()

    if ' 7 ' in chos:

        cpr.printblue("Select the file to open :")
        cpr.resetcolor()
        filelocation = filedialog.askopenfilename(
            title='Select file',
        )
        # cleaning the screen ...
        clear()


    if ' 8 ' in chos:

        cpr.printblue("Enter the link : ")
        cpr.resetcolor()
        link = input()
        cpr.resetcolor()
        # cleaning the screen ...
        clear()


    cpr.printred('Hide consle when time running ? (Y/N) : ')
    cpr.resetcolor()
    con = input()
    if 'Y' in con or 'y' in con:
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)

    # cleaning the screen ...
    clear()


    total = h*3600+m*60+s
    h = int(total/3600)
    m = int((total%3600)/60)
    s = total%60

    if m < 10 : mm = ('0'+str(m))

    else : mm = str(m)
        
    if s < 10:ss = ('0'+str(s))
        
    else :ss = str(s)

    cpr.printblue("The Required Time → " +str(h)+":"+str(mm)+":"+str(ss))

    # print all required things ↓

    if ' 1 ' in chos:cpr.printred("\nShutdown The PC\n")

    if ' 2 ' in chos:cpr.printred("\nRestart The PC\n")

    if ' 3 ' in chos:cpr.printred("\nSleep\n")

    if ' 4 ' in chos:cpr.printred("\nSend a notification → " +notnam+"\n")

    if ' 5 ' in chos:cpr.printred("\nSign out\n")

    if ' 6 ' in chos:cpr.printred("\nPlay music → " +orr+"\n")

    if ' 7 ' in chos:cpr.printred("\nOpen file → " +filelocation+"\n")

    if ' 8 ' in chos:cpr.printred("\nOpen link in browser → " +link+"\n")

    if ' 9 ' in chos:cpr.printred("\nRun CMD command → " +comm+"\n")

    if chos == '00':cpr.printred("\nNothing\n")


    cpr.printaqua("")
    countdown(int(h), int(m), int(s))


    # cleaning the screen ...
    clear()



    #                                  =================== AFTER THE TIMES IS UP ===================



    if ' 1 ' in chos :system("shutdown /s /t 0")                                       # shutting down                            
    if ' 2 ' in chos :system("shutdown /r /t 0")                                       # restarting                               
    if ' 5 ' in chos :system("shutdown /l")                                            # signing out                              
    if ' 3 ' in chos :system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")        # sleeping mode                            
    if ' 4 ' in chos:                                                                     # sening the notification                  
        if iconn != '':                                                           # if there is icon notification settings   
            notification.notify(
            title = notnam,
            message = masg,
            timeout = 10,
            app_icon = iconn,
            )
        else :                                                                            # if there is no icon notification settings
            notification.notify(
            title = notnam,
            message = masg,
            timeout = 10,
            )
    if ' 7 ' in chos :startfile(filelocation)                                          # opening ordered file                     
    if ' 8 ' in chos :open(link)                                                          # opening ordered link                     
    if ' 9 ' in chos :system(comm)                                                     # running the command                      
    if ' 6 ' in chos :                                                                    # playing the music file                   
        clear()
        pygame.init()
        pygame.mixer.music.load(orr)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():pass
