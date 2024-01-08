import datetime
import threading
import tkinter as tk

import pandas as pd

from Create_Button import button_return, button_export_NIR, button_export_VIS, button_select_VIS, button_select_NIR, \
    button_get_data
from Create_Clock import clock
from PIL import ImageTk, Image

from Create_Entry import entry_box_calib, entry_box_data, entry_box_mean_spectrum
from Create_Label import label_title_spectrum, label_title_training, label_title_export_calib, label_title_export_data, \
    label_title_export_mean_spectrum, label_title_about
from Export_calib_nir import Export_calib_nir
from Export_calib_vis import Export_calib_vis
from Export_data_nir import Export_Data_nir
from Export_data_vis import Export_Data_vis
from Mean_spectrum import mean_features


def Training():
    windows = tk.Toplevel()
    windows.geometry("1720x900")
    windows.resizable(width=False, height=False)
    windows.title('Training model')

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_bot = tk.Frame(windows, bg='Gray', width=800, height=5)
    frame_bot.grid(row=1, column=0, sticky="nsew")

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_training(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    def end_win_spectrum_plot():
        windows.destroy()

    # Tạo nút
    btn_return_threading = threading.Thread(target=button_return(frame_top, click=end_win_spectrum_plot))
    btn_return_threading.start()

    windows.update()


def Spectrum():
    windows = tk.Toplevel()
    windows.geometry("1720x900")
    # windows.resizable(width=False, height=False)
    windows.title('Spectrum plot')

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_bot = tk.Frame(windows, bg='Gray', width=800, height=5)
    frame_bot.grid(row=1, column=0, sticky="nsew")

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_spectrum(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    def end_win_spectrum_plot():
        windows.destroy()

    # Tạo nút
    btn_return_threading = threading.Thread(target=button_return(frame_top, click=end_win_spectrum_plot))
    btn_return_threading.start()

    windows.update()


def Export_data():
    windows = tk.Toplevel()
    windows.geometry("1520x768")
    windows.resizable(width=False, height=False)
    windows.title('Export data')

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_bot = tk.Frame(windows, bg='Gray', width=800, height=5)
    frame_bot.grid(row=1, column=0, sticky="nsew")
    frame_bot_left = tk.Frame(frame_bot, bg='gray')
    frame_bot_left.pack(side='left', pady=5, padx=10)
    frame_bot_right = tk.Frame(frame_bot, bg='gray')
    frame_bot_right.pack(side='right', pady=5, padx=10)

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_export_data(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    def end_win_spectrum_plot():
        windows.destroy()

    # Tạo nút
    btn_return_threading = threading.Thread(target=button_return(frame_top, click=end_win_spectrum_plot))
    btn_return_threading.start()

    def click_export_vis():
        # -----------------------------------------------------
        frame_top_vis = tk.Frame(frame_bot_left, bg='White', width=50, height=5)
        frame_top_vis.pack()
        frame_bot_vis = tk.Frame(frame_bot_left, bg='Gray', width=50, height=5)
        frame_bot_vis.pack()

        title_lb = tk.Label(frame_top_vis, text="EXPORT DATA (VIS)", font=("TVN-Qatar2022-Bold", 15),
                            background='Gray', foreground='red', borderwidth=0, border=0, width=61)
        title_lb.pack()

        # -----------------------------------------------------
        (values_path_folder_sensor, values_name_file,
         values_path_save_file, values_path_calib_file, values_cultivar) = entry_box_data(frame_bot_vis)

        def export_vis():
            global label_show_vis_data
            value_path_folder = values_path_folder_sensor.get()
            value_name = values_name_file.get()
            value_path_save = values_path_save_file.get()
            value_path_calib = values_path_calib_file.get()
            cultivar = values_cultivar.get()

            Export_Data_vis(file_name=f'{value_name}', path_folder_sensor=value_path_folder, path_save=value_path_save,
                            path_calib_file=value_path_calib, cultivar_name=f'{cultivar}')

            try:
                if label_show_vis_data:
                    label_show_vis_data.destroy()  # Xóa label nếu đã tồn tại
            except:
                pass
            label_show_vis_data = tk.Label(frame_bot_vis, text=f'Đã Xuất File đến: {value_path_save}',
                                           font=('TVN-Qatar2022-Bold', 15),
                                           bg='Gray')
            label_show_vis_data.pack()

        btn_export_vis_thread = threading.Thread(target=button_export_NIR(frame_bot_vis, click=export_vis))
        btn_export_vis_thread.start()

    # -----------------------------------------------------
    def click_export_nir():
        # -----------------------------------------------------
        frame_top_vis = tk.Frame(frame_bot_right, bg='White', width=50, height=5)
        frame_top_vis.pack()
        frame_bot_vis = tk.Frame(frame_bot_right, bg='Gray', width=50, height=5)
        frame_bot_vis.pack()

        title_lb = tk.Label(frame_top_vis, text="EXPORT DATA (NIR)", font=("TVN-Qatar2022-Bold", 15),
                            background='Gray', foreground='red', borderwidth=0, border=0, width=61)
        title_lb.pack()

        # -----------------------------------------------------
        (values_path_folder_sensor, values_name_file,
         values_path_save_file, values_path_calib_file, values_cultivar) = entry_box_data(frame_bot_vis)

        def export_nir():
            global label_show_nir_data
            value_path_folder = values_path_folder_sensor.get()
            value_name = values_name_file.get()
            value_path_save = values_path_save_file.get()
            value_path_calib = values_path_calib_file.get()
            cultivar = values_cultivar.get()

            Export_Data_nir(file_name=f'{value_name}', path_folder_sensor=value_path_folder,
                            path_save=value_path_save, path_calib_file=value_path_calib,
                            cultivar_name=f'{cultivar}')

            try:
                if label_show_nir_data:
                    label_show_nir_data.destroy()  # Xóa label nếu đã tồn tại
            except:
                pass
            label_show_nir_data = tk.Label(frame_bot_vis, text=f'Đã Xuất File đến: {value_path_save}',
                                           font=('TVN-Qatar2022-Bold', 15),
                                           bg='Gray')
            label_show_nir_data.pack()

        btn_export_nir_thread = threading.Thread(target=button_export_NIR(frame_bot_vis, click=export_nir))
        btn_export_nir_thread.start()

    click_export_vis()
    click_export_nir()

    windows.update()


def Export_calib():
    windows = tk.Toplevel()
    windows.geometry("1520x568")
    windows.resizable(width=False, height=False)
    windows.title('Export calib')

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_bot = tk.Frame(windows, bg='Gray', width=800, height=5)
    frame_bot.grid(row=1, column=0, sticky="nsew")
    frame_bot_left = tk.Frame(frame_bot, bg='gray')
    frame_bot_left.pack(side='left', pady=5)
    frame_bot_right = tk.Frame(frame_bot, bg='gray')
    frame_bot_right.pack(side='right', pady=5)

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_export_calib(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    def end_win_spectrum_plot():
        windows.destroy()

    # Tạo nút
    btn_return_threading = threading.Thread(target=button_return(frame_top, click=end_win_spectrum_plot))
    btn_return_threading.start()

    def click_export_vis():
        # -----------------------------------------------------
        frame_top_vis = tk.Frame(frame_bot_left, bg='White')
        frame_top_vis.pack()
        frame_bot_vis = tk.Frame(frame_bot_left, bg='Gray')
        frame_bot_vis.pack()

        # -----------------------------------------------------
        title_lb = tk.Label(frame_top_vis, text="EXPORT CALIB (VIS)", font=("TVN-Qatar2022-Bold", 15),
                            background='gray', foreground='red', borderwidth=0, border=0, width=61)
        title_lb.pack()

        values_path_folder, values_name_file, values_path_save_file = entry_box_calib(frame_bot_vis)

        def click_data():
            global label_show_vis
            value_path_folder = values_path_folder.get()
            print("Đã nhận:", value_path_folder)
            value_name = values_name_file.get()
            print("Đã nhận:", value_name)
            value_path_save = values_path_save_file.get()
            print("Đã nhận:", value_path_save)

            Export_calib_vis(path_folder=value_path_folder, name_file=f'{value_name}', path_save=value_path_save)
            try:
                if label_show_vis:
                    label_show_vis.destroy()  # Xóa label nếu đã tồn tại
            except:
                pass
            label_show_vis = tk.Label(frame_bot_vis, text=f'Đã Xuất File đến: {value_path_save}',
                                      font=('TVN-Qatar2022-Bold', 15),
                                      bg='Gray')
            label_show_vis.pack()

        # Tạo nút export data
        btn_export_threading = threading.Thread(target=button_export_VIS(frame_bot_vis, click_data))
        btn_export_threading.start()

    def click_export_nir():
        # -----------------------------------------------------
        frame_top_nir = tk.Frame(frame_bot_right, bg='White')
        frame_top_nir.pack()
        frame_bot_nir = tk.Frame(frame_bot_right, bg='Gray')
        frame_bot_nir.pack()

        # -----------------------------------------------------
        title_lb = tk.Label(frame_top_nir, text="EXPORT CALIB (NIR)", font=("TVN-Qatar2022-Bold", 15),
                            background='gray', foreground='red', borderwidth=0, border=0, width=61)
        title_lb.pack()

        # ----------------------------------------------------
        values_path_folder, values_name_file, values_path_save_file = entry_box_calib(frame_bot_nir)

        def click_data():
            global label_show_nir
            value_path_folder = values_path_folder.get()
            print("Đã nhận:", value_path_folder)
            value_name = values_name_file.get()
            print("Đã nhận:", value_name)
            value_path_save = values_path_save_file.get()
            print("Đã nhận:", value_path_save)

            Export_calib_nir(path_folder=value_path_folder, name_file=f'{value_name}', path_save=value_path_save)
            try:
                if label_show_nir:
                    label_show_nir.destroy()  # Xóa label nếu đã tồn tại
            except:
                pass
            label_show_nir = tk.Label(frame_bot_nir, text=f'Đã Xuất File đến: {value_path_save}',
                                      font=('TVN-Qatar2022-Bold', 15),
                                      bg='Gray')
            label_show_nir.pack()

        # Tạo nút export data
        btn_export_threading = threading.Thread(target=button_export_NIR(frame_bot_nir, click_data))
        btn_export_threading.start()

    click_export_vis()
    click_export_nir()

    windows.update()


def Export_mean_spectrum():
    windows = tk.Toplevel()
    windows.geometry("750x620")
    windows.resizable(width=False, height=False)
    windows.title('Export mean spectrum')

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_bot = tk.Frame(windows, bg='Gray', width=800, height=5)
    frame_bot.grid(row=1, column=0, sticky="nsew")

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_export_mean_spectrum(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    def end_win_spectrum_plot():
        windows.destroy()

    # Tạo nút
    btn_return_threading = threading.Thread(target=button_return(frame_top, click=end_win_spectrum_plot))
    btn_return_threading.start()

    values_path_file_data, values_name_file, values_path_save_file, values_start_col = entry_box_mean_spectrum(frame_bot)

    def click_export():
        global label_show_mean_spectrum
        value_path_folder = values_path_file_data.get()
        value_name = values_name_file.get()
        value_path_save = values_path_save_file.get()
        values_col = values_start_col.get()
        values_col = int(values_col)

        df = pd.read_csv(fr"{value_path_folder}")
        path_s = value_path_save + fr'\{value_name}.csv'

        mean_features(df, path_save_file=path_s, start_col=values_col)
        try:
            if label_show_mean_spectrum:
                label_show_mean_spectrum.destroy()  # Xóa label nếu đã tồn tại
        except:
            pass
        label_show_mean_spectrum = tk.Label(frame_bot, text=f'Đã Xuất File đến: {value_path_save}',
                              font=('TVN-Qatar2022-Bold', 15),
                              bg='Gray')
        label_show_mean_spectrum.pack()

    btn_export = threading.Thread(target=button_get_data(frame_bot, click_export))
    btn_export.start()

    windows.update()


def About():
    windows = tk.Toplevel()
    windows.geometry("720x520")
    windows.resizable(width=False, height=False)
    windows.title('About')

    windows.grid_rowconfigure(0, weight=1)
    windows.grid_rowconfigure(1, weight=50)
    windows.grid_columnconfigure(0, weight=1)

    frame_top = tk.Frame(windows, bg='White', width=50, height=5)
    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_bot = tk.Frame(windows, bg='Gray', width=800, height=5)
    frame_bot.grid(row=1, column=0, sticky="nsew")

    # Tạo tựa windows
    lb_title_threading = threading.Thread(target=label_title_about(frame_top))
    lb_title_threading.start()

    # Tạo đồng hồ
    clock_threading = threading.Thread(target=clock(frame_top))
    clock_threading.start()

    def end_win_spectrum_plot():
        windows.destroy()

    # Tạo nút
    btn_return_threading = threading.Thread(target=button_return(frame_top, click=end_win_spectrum_plot))
    btn_return_threading.start()

    windows.update()
