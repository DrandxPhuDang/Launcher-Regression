import threading
import tkinter as tk
from Create_Label import label_title_select
from Create_Button import (button_sign_out, button_export_data, button_export_calib, button_export_mean_spectrum,
                           button_spectrum_plot, button_training_model)
from Create_Clock import clock
from Create_Windows import Spectrum, Training, Export_calib, Export_data, Export_mean_spectrum


def frame_top_training(windows):
    # Frame top
    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_select(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    # Tạo nút đăng xuất
    btn_sign_out_threading = threading.Thread(target=button_sign_out(frame_top))
    btn_sign_out_threading.start()


def frame_bot_training(windows):
    # Frame bot
    frame_bot = tk.Frame(windows, bg='Light Gray')
    frame_bot.grid(row=1, column=0, sticky="nsew")

    def click_calib():
        Export_calib()

    def click_data():
        Export_data()

    def click_mean_spectrum():
        Export_mean_spectrum()

    def click_spectrum_plot():
        Spectrum()

    def click_training_model():
        Training()

    # Tạo nút
    btn_export_calib_threading = threading.Thread(target=button_export_calib(frame_bot, click=click_calib))
    btn_export_calib_threading.start()

    # Tạo nút
    btn_export_data_threading = threading.Thread(target=button_export_data(frame_bot, click=click_data))
    btn_export_data_threading.start()

    # Tạo nút
    btn_mean_spectrum_threading = threading.Thread(target=button_export_mean_spectrum(frame_bot,
                                                                                      click=click_mean_spectrum))
    btn_mean_spectrum_threading.start()

    # Tạo nút
    btn_spectrum_plot_threading = threading.Thread(target=button_spectrum_plot(frame_bot,
                                                                                      click=click_spectrum_plot))
    btn_spectrum_plot_threading.start()

    # Tạo nút
    btn_training_model_threading = threading.Thread(target=button_training_model(frame_bot,
                                                                                      click=click_training_model))
    btn_training_model_threading.start()
