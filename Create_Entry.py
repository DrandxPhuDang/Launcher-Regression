import tkinter as tk


def entry_box_calib(windows):
    # Tạo text box đầu vào
    path_folder_sensor = tk.Label(windows, text="Path Folder Sensor", font=("TVN-Qatar2022-Bold", 15), bg='gray',
                                  fg='White')
    path_folder_sensor.pack()
    values_path_folder_sensor = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_folder_sensor.pack()

    # Tạo text box đầu ra
    name_file = tk.Label(windows, text="Name File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    name_file.pack()
    values_name_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_name_file.pack()

    # Tạo text box đầu ra
    path_save_file = tk.Label(windows, text="Path Save File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    path_save_file.pack()
    values_path_save_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_save_file.pack()

    return values_path_folder_sensor, values_name_file, values_path_save_file


def entry_box_data(windows):
    # Tạo text box đầu vào
    path_folder_sensor = tk.Label(windows, text="Path Folder Sensor", font=("TVN-Qatar2022-Bold", 15), bg='gray',
                                  fg='White')
    path_folder_sensor.pack()
    values_path_folder_sensor = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_folder_sensor.pack()

    # Tạo text box đầu ra
    name_file = tk.Label(windows, text="Name File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    name_file.pack()
    values_name_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_name_file.pack()

    # Tạo text box đầu ra
    path_save_file = tk.Label(windows, text="Path Save File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    path_save_file.pack()
    values_path_save_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_save_file.pack()

    # Tạo text box đầu ra
    path_calib_file = tk.Label(windows, text="Path Calib File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    path_calib_file.pack()
    values_path_calib_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_calib_file.pack()

    # Tạo text box đầu ra
    cultivar = tk.Label(windows, text="Path Cultivar", font=("TVN-Qatar2022-Bold", 15), bg='gray',
                        fg='White')
    cultivar.pack()
    values_cultivar = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_cultivar.pack()

    return values_path_folder_sensor, values_name_file, values_path_save_file, values_path_calib_file, values_cultivar


def entry_box_mean_spectrum(windows):
    # Tạo text box đầu vào
    path_folder_sensor = tk.Label(windows, text="Path File Data", font=("TVN-Qatar2022-Bold", 15), bg='gray',
                                  fg='White')
    path_folder_sensor.pack()
    values_path_folder_sensor = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_folder_sensor.pack()

    # Tạo text box đầu ra
    name_file = tk.Label(windows, text="Name File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    name_file.pack()
    values_name_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_name_file.pack()

    # Tạo text box đầu ra
    path_save_file = tk.Label(windows, text="Path Save File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    path_save_file.pack()
    values_path_save_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_save_file.pack()

    # Tạo text box đầu ra
    start_col = tk.Label(windows, text="Start Column", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    start_col.pack()
    values_start_col = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_start_col.pack()

    return values_path_folder_sensor, values_name_file, values_path_save_file, values_start_col


def entry_box_spectrum_plot(windows):
    # Tạo text box đầu vào
    path_folder_sensor = tk.Label(windows, text="Path File Data", font=("TVN-Qatar2022-Bold", 15), bg='gray',
                                  fg='White')
    path_folder_sensor.pack()
    values_path_folder_sensor = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_folder_sensor.pack()

    # Tạo text box đầu ra
    path_save_file = tk.Label(windows, text="Path Save File", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    path_save_file.pack()
    values_path_save_file = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_save_file.pack()

    # Tạo text box đầu ra
    start_col = tk.Label(windows, text="Start Column", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    start_col.pack()
    values_start_col = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_start_col.pack()

    # Tạo text box đầu ra
    Plot = tk.Label(windows, text="Num Plot", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    Plot.pack()
    values_Plot = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_Plot.pack()

    object = tk.Label(windows, text="Object", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    object.pack()
    values_object = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_object.pack()

    list_object = tk.Label(windows, text="List Object", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    list_object.pack()
    values_list_object = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_list_object.pack()

    target = tk.Label(windows, text="Target", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    target.pack()
    values_target = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_target.pack()

    return (values_path_folder_sensor, values_path_save_file, values_start_col,
            values_Plot, values_object, values_list_object, values_target)


def entry_box_spectrum_mini_plot(windows):
    # Tạo text box đầu vào
    path_File = tk.Label(windows, text="Path File Data", font=("TVN-Qatar2022-Bold", 15), bg='gray',
                         fg='White')
    path_File.pack()
    values_path_File = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_path_File.pack()

    # Tạo text box đầu ra
    Start = tk.Label(windows, text="Start Column", font=("TVN-Qatar2022-Bold", 15), bg='gray', fg='White')
    Start.pack()
    values_Start = tk.Entry(windows, font=("TVN-Qatar2022-Bold", 20), width=40)
    values_Start.pack()

    return values_path_File, values_Start
