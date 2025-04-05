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

    # Initialize Tkinter window
root = tk.Tk()
root.title('Digital Clock')
root.geometry('500x300')  # Adjusted window size

#Create label for clock display
label_hr = tk.Label(root, font=("calibri", 40, "bold"), bg='black', fg='white')
label_hr.place(x=100, y=100, width=300, height=100)  # Centered position

# Start updating time
update_time()

# Run the Tkinter event loop
root.mainloop()
