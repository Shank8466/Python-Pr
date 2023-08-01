# Import Required Library
from tkinter import *
import datetime
import time
import threading
import winsound

# Create Object
root = Tk()

# Set geometry
root.geometry("400x250")

# Global Variables
alarm_on = False
snooze_time = 300  # Default snooze time is 5 minutes (300 seconds)

# Use Threading
def Threading():
    global alarm_on
    alarm_on = True
    t1 = threading.Thread(target=alarm)
    t1.start()

def alarm():
    global alarm_on
    # Infinite Loop
    while alarm_on:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to do your work")
            # Buzzing alarm
            for _ in range(3):  # Buzz 3 times
                winsound.Beep(1000, 1000)  # Beep with 1000Hz for 1 second each
            snooze_button.config(state=NORMAL)

def snooze():
    global alarm_on
    global snooze_time
    alarm_on = False  # Disable the alarm
    snooze_time = int(snooze_minutes.get()) * 60  # Get snooze time in seconds
    # Disable snooze button to prevent multiple snoozes
    snooze_button.config(state=DISABLED)
    # Wait for the snooze time
    time.sleep(snooze_time)
    # Resume the alarm
    Threading()

# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="black").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = tuple(f"{i:02d}" for i in range(60))
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = tuple(f"{i:02d}" for i in range(60))
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Snooze section
Label(root, text="Snooze Time (minutes)", font=("Helvetica 15 bold")).pack()
snooze_minutes = StringVar(root)
snooze_minutes.set("5")  # Default snooze time is 5 minutes

snooze_time_menu = OptionMenu(root, snooze_minutes, *list(range(1, 61)))
snooze_time_menu.pack()

snooze_button = Button(root, text="Snooze", font=("Helvetica 15"), state=DISABLED, command=snooze)
snooze_button.pack(pady=10)

# Execute Tkinter
root.mainloop()
  