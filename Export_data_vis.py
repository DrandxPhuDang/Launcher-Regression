import os
import time

import numpy as np
import pandas as pd


class Export_Data_vis:
    def __init__(self, file_name, path_folder_sensor, path_save, cultivar_name, path_calib_file):
        super().__init__()
        self.path_folder = fr'{path_folder_sensor}'
        self.path_folder_save = fr'{path_save}'
        self.path_save_file = self.path_folder_save + fr'\{file_name}.csv'

        def Get_data(path):
            """
            :param path: Thư mục chứa các file csv từ cảm biến
            :return: Trả về tên file và giá trị trong file
            """
            global waves
            os.chdir(path)
            files = sorted(os.listdir(path))
            name_csv = []
            for f in files:
                if f.endswith('.csv'):
                    name_csv.append(f)
            df = pd.DataFrame()
            for f in name_csv:
                data = pd.read_csv(f, skiprows=[i for i in range(0, 4)])
                waves = data.iloc[:, 0].values
                values = data.iloc[:, 1].values
                values = pd.DataFrame(values).T
                df = pd.concat([df, values])
            df = pd.DataFrame(np.array(df), columns=waves)
            waves = pd.DataFrame(np.array(waves))
            return waves, df, name_csv

        def Reference(calib_data, signal_data):
            """
            :param calib_data: Nhập giá trị từ file calibration (Final.... .cvs)
            :param signal_data: Nhập giá trị cột signal của file csv cảm biến
            :return: Giá trị đã tính toán với công thức là signal/calib
            """
            bien_dem = 0
            values_calib = []
            values_calib_2 = []
            for list_sig_data in signal_data.values:
                for sig_data in list_sig_data:
                    for clib in calib_data.values[bien_dem]:
                        ref_data = sig_data / clib
                        values_calib.append([ref_data])
                    bien_dem = bien_dem + 1
                bien_dem = 0
                values_calib = pd.DataFrame(values_calib).T
                values_calib_2 = pd.DataFrame(values_calib_2)._append([values_calib])
                values_calib = []
            return values_calib_2

        features, data, name_data = Get_data(self.path_folder)
        listWavelength = features.values[0:, 0].tolist()

        data_calib = pd.read_csv(path_calib_file)
        data_calib = pd.DataFrame(data_calib)
        data_calib = data_calib.T

        data_ref = Reference(data_calib, data)
        self.final_Data = pd.DataFrame(np.array(data_ref), columns=listWavelength)

        def export_excel():
            """
            :return: Hàm xử lí pandas chèn tên cột và các giá trị tương ứng
            """
            Cultivar_data = []
            Date = []
            Brix = []
            Acid = []
            Ratio = []
            Number = []
            Point = []
            Area = []

            for name in name_data:
                name = name.replace('_', '')
                if name[0] == 'e':
                    Number.append(name[1:4])
                    Area.append(name[8])
                    Point.append(name[6:8])
                    Date.append(name[9:19])
                    Brix.append(name[1])
                    Acid.append(name[1])
                    Ratio.append(name[1])
                if name[0] != 'e':
                    Cultivar_data = cultivar_name
                    Number.append(name[1:4])
                    Area.append(name[8])
                    Point.append(name[6:8])
                    Date.append(name[9:19])
                    Brix.append(name[1])
                    Acid.append(name[1])
                    Ratio.append(name[1])

            self.final_Data.insert(loc=0, column='Ratio', value=Ratio)
            self.final_Data.insert(loc=0, column='Acid', value=Acid)
            self.final_Data.insert(loc=0, column='Brix', value=Brix)
            self.final_Data.insert(loc=0, column='Point', value=Point)
            self.final_Data.insert(loc=0, column='Area', value=Area)
            self.final_Data.insert(loc=0, column='Date', value=Date)
            self.final_Data.insert(loc=0, column='Number', value=Number)
            self.final_Data.insert(loc=0, column='Cultivar', value=Cultivar_data)

            self.final_Data.to_csv(self.path_save_file, index=False, header=True, na_rep='Unknown')

            print(f'Successful export data excel to {self.path_folder_save}')

        export_excel()
