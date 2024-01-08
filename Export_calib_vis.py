import pandas as pd
import numpy as np
import os


class Export_calib_vis:
    def __init__(self, path_folder, name_file, path_save):
        super().__init__()

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

        features, data, name_data = Get_data(path_folder)
        listWavelength = features.values[0:, 0].tolist()

        list_number = []
        for call_name in name_data:
            call_name = call_name.replace('_', '')
            if call_name[0] == 'e':
                list_number.append(call_name[1])
            if call_name[0] != 'e':
                list_number.append(call_name[1])

        data.to_csv(path_save + r'\signal_data_calibration ' + name_file + '.csv',
                          index=False, header=True, na_rep='Unknown')

        tb_data = pd.read_csv(path_save + r'\signal_data_calibration ' + name_file + '.csv')

        list_tb_cong = []
        for v in listWavelength:
            answer = 0
            mylist = tb_data[f'{v}'].tolist()
            for n in mylist:
                answer += n
            answer = answer / len(name_data)
            answer = round(answer)
            list_tb_cong.append([answer])

        list_tb_cong = np.array(pd.DataFrame(list_tb_cong).T)
        list_tb_cong = pd.DataFrame(list_tb_cong, columns=listWavelength)

        list_tb_cong.to_csv(path_save + r'\final_data_calibration ' + name_file + '.csv',
                            index=False, header=True, na_rep='Unknown')