from ctypes import windll
from sys import stdout
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12



FOREGROUND_BLUE = 0x01  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_RED = 0x04  # red.
FOREGROUND_YELLOW = 0x06  # yellow.
FOREGROUND_WHITE = 0x0f  # white.
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_AQUA = 0x0b  # aqua.
FOREGROUND_PURPLE = 0x05  # purple.

# background color define
BACKGROUND_YELLOW = 0xe0  # yellow.

# get handle
std_out_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetcolor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


# green
def printgreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    stdout.write(mess + '\n')
    

#black
def printblack(mess):
    set_cmd_text_color(FOREGROUND_BLACK)
    stdout.write(mess + '\n')
    
#aqua
def printaqua(mess):
    set_cmd_text_color(FOREGROUND_AQUA)
    stdout.write(mess + '\n')
    
#purple
def printpurple(mess):
    set_cmd_text_color(FOREGROUND_PURPLE)
    stdout.write(mess + '\n')
    

# red
def printred(mess):
    set_cmd_text_color(FOREGROUND_RED)
    stdout.write(mess + '\n')
    

# yellow
def printyellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    stdout.write(mess + '\n')
    

# white bkground and black text
def printyellowred(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    stdout.write(mess + '\n')
    
#white
def printwhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    stdout.write(mess + '\n')
    
#blue
def printblue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    stdout.write(mess + '\n')

