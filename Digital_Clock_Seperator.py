import tkinter as tk
import time

def update_time():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    
    # Update label text with full time
    label_hr.config(text=f"{h}:{m}:{s}")  
    
    # Call this function again after 1000ms (1 second)
    label_hr.after(1000, update_time)