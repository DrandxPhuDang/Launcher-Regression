import tkinter as tk


def menu_box_spectrum_plot(window, spectrum_mini):
    # Tạo một menu bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # Tạo một menu box
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Thêm các lệnh vào menu box
    file_menu.add_command(label="Spectrum object", command=spectrum_mini)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
