import datetime
import tkinter as tk


def clock(frame):
    def date_time():
        s_time = datetime.datetime.now().strftime('%H:%M:%S, %d-%m-%Y')
        s_time = f'{s_time}'
        time_lb.config(text=s_time)
        time_lb.after(10, date_time)

    time_lb = tk.Label(frame, fg='Black', bg='white', font=("Arial", 10))
    time_lb.pack()
    date_time()
