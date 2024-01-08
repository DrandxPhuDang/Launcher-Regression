import threading
import tkinter as tk
from Create_Frame import frame_top_training, frame_bot_training


def main_page():
    windows = tk.Tk()

    windows.geometry("360x540")
    windows.title("Select mode")
    windows.resizable(width=False, height=False)
    icon = tk.PhotoImage(file=r"image\logo.png")
    windows.iconphoto(True, icon)

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    # Create frame in windows
    frame_top_thread = threading.Thread(target=frame_top_training(windows))
    frame_bot_thread = threading.Thread(target=frame_bot_training(windows))
    frame_top_thread.start()
    frame_bot_thread.start()

    windows.mainloop()


main_page()
