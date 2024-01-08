import tkinter as tk


def button_sign_out(frame, click):
    btn_sign_out = tk.Button(frame, text="SIGN OUT",
                             font=('TVN-Qatar2022-Bold', 10), bg='white', activebackground='white',
                             fg='white', foreground='black', border=0, command=click)
    btn_sign_out.place(x=0, y=0)


def button_return(frame, click):
    btn = tk.Button(frame, text="RETURN",
                    font=('TVN-Qatar2022-Bold', 10), bg='white', activebackground='white',
                    fg='white', foreground='black', border=0, command=click)
    btn.place(x=0, y=0)


def button_export_calib(frame, click):
    btn = tk.Button(frame, text="EXPORT CALIB", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                    activebackground='black', fg='white', activeforeground='White', command=click, width=25)
    btn.pack(pady=15)


def button_export_data(frame, click):
    btn = tk.Button(frame, text="EXPORT DATA", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                    activebackground='black', fg='white', activeforeground='White', command=click, width=25)
    btn.pack(pady=15)


def button_export_mean_spectrum(frame, click):
    btn = tk.Button(frame, text="EXPORT MEAN SPECTRUM", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                    activebackground='black', fg='white', activeforeground='White', command=click, width=25)
    btn.pack(pady=15)


def button_spectrum_plot(frame, click):
    btn = tk.Button(frame, text="SPECTRUM PLOT", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                    activebackground='black', fg='white', activeforeground='White', command=click, width=25)
    btn.pack(pady=15)


def button_training_model(frame, click):
    btn = tk.Button(frame, text="TRAINING MODEL", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                    activebackground='black', fg='white', activeforeground='White', command=click, width=25)
    btn.pack(pady=15)


def button_select_VIS(frame, click):
    btn_sign_out = tk.Button(frame, text="EXPORT CALIB (VIS)", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                             activebackground='black', fg='white', activeforeground='White', command=click)
    btn_sign_out.pack(pady=15)


def button_select_NIR(frame, click):
    btn_sign_out = tk.Button(frame, text="EXPORT CALIB (NIR)", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                             activebackground='black', fg='white', activeforeground='White', command=click)
    btn_sign_out.pack(pady=20)


def button_export_VIS(frame, click):
    btn_sign_out = tk.Button(frame, text="EXPORT DATA", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                             activebackground='black', fg='white', activeforeground='White', command=click)
    btn_sign_out.pack(pady=15)


def button_export_NIR(frame, click):
    btn_sign_out = tk.Button(frame, text="EXPORT DATA", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                             activebackground='black', fg='white', activeforeground='White', command=click)
    btn_sign_out.pack(pady=20)


def button_get_data(frame, click):
    btn_get_data = tk.Button(frame, text="EXPORT DATA", border=2, font=('TVN-Qatar2022-Bold', 15), bg='Gray',
                             activebackground='black', fg='white', activeforeground='White', command=click)
    btn_get_data.pack(pady=15)

