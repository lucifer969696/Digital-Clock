#!/usr/bin/env python
# coding: utf-8

# In[1]:


#We start by importing the necessary modules: tkinter for the GUI and time for the clock functionality.

import tkinter as tk 
import time

#The update_clock function gets the current time in the format of "HH:MM:SS" using the strftime method and updates the text of the clock label. 
#It also schedules the function to run again after 1000 milliseconds (i.e. 1 second) using the after method.

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)
#We create a Tkinter window and a Label widget to display the clock.
root = tk.Tk()
root.title('Digital Clock')
clock_label = tk.Label(root, font=('Arial', 80), bg='black', fg='white')
clock_label.pack(fill='both', expand=True)
update_clock()      #We call the update_clock function to start the clock, and then run the main loop of the GUI using root.mainloop().
root.mainloop()


#When you run this code, a window will open with a large digital clock displaying the current time. 
#The clock will update every second to show the correct time. 
#we can customize the appearance of the clock by changing the font, color, and size of the label.


# In[ ]:




