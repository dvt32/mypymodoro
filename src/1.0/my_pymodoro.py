from __future__ import print_function
from colorama import *
import webbrowser
import sys
import time

# Initialize colored output and set colors
init()

# Get settings from file
file = open('settings.txt', 'r')
settings = file.readlines()
file.close()

# Set timer in seconds
pomodoro = int(settings[1])*60

# Set URL to open
url = settings[4]

# Header
print(" ----------------- ")
print(Fore.GREEN + "  MyPymodoro v1.0 " + Style.RESET_ALL)
print(" ----------------- ")
print(Fore.YELLOW + " http://dvt32.blogspot.com/\n" + Style.RESET_ALL)

# Time left information
print (" Timer started! Break coming up in " + Back.RED + str(pomodoro / 60) + " minutes" + Style.RESET_ALL + "!\n")

# Print time elapsed
for second in range(pomodoro):
    print (" Time left until break: " +
           Fore.YELLOW +
           str(pomodoro / 60) + " minute(s), " +
           str(pomodoro % 60) + " seconds" + " " +
           Style.RESET_ALL,
           end="\r")
    sys.stdout.flush()
    pomodoro -= 1
    time.sleep(1)

# Load video after time is up
webbrowser.open(url)
