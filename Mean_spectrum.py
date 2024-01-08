import numpy as np
import pandas as pd


def mean_features(df, path_save_file, start_col):
    """
    :param df: file data csv đo ngẫu nhiên
    :param path_save_file: địa chỉ lưu file
    :param start_col: số cột bắt đầu
    :return: data frame đã tính trung bình phổ 3 điểm
    """
    # ----------------- get number -----------------------
    def get_number(data):
        data_area = data[data['Area'] == 'A']
        data_point = data_area[data_area['Point'] == 1]
        data_number = data_point['Number']
        return data_number

    # ----------------- get area -----------------------
    def get_area(number):
        data_number = df[df['Number'] == number]
        data_point = data_number[data_number['Point'] == 1]
        data_area = data_point['Area']
        return data_area

    # ----------------- get brix -----------------------
    def get_brix(data):
        data_point = data[data['Point'] == 1]
        data_brix = data_point['Brix']
        return data_brix

    def get_acid(data):
        data_point = data[data['Point'] == 1]
        data_acid = data_point['Acid']
        return data_acid

    def get_ratio(data):
        data_point = data[data['Point'] == 1]
        data_ratio = data_point['Ratio']
        return data_ratio

    list_features = df.iloc[:0, start_col:]
    features = [f'{e}' for e in list_features]
    Features_col_all = pd.DataFrame()
    List_number = []
    for num in get_number(df):
        list_all = []
        for area in get_area(num):
            List_number.append(num)
            df_dt = df[df['Number'] == num]
            df_dt = df_dt[df_dt['Area'] == area]
            features_col = df_dt[features]
            list_mean = []
            mean = 0
            for i in features:
                for j in features_col[i].values:
                    mean = j + mean
                mean = mean / len(features_col[i].values)
                list_mean.append(mean)
                mean = 0
            list_all.append(list_mean)
        Features_col = pd.DataFrame(np.array(list_all), columns=features)
        Features_col_all = pd.DataFrame(Features_col_all)._append([Features_col])

    Features_col_all = Features_col_all.reset_index(drop=True)
    df_brix = get_brix(df).reset_index(drop=True)
    df_acid = get_acid(df).reset_index(drop=True)
    df_ratio = get_ratio(df).reset_index(drop=True)
    df_number = pd.DataFrame(np.array(List_number), columns=['Number']).reset_index(drop=True)

    Features_col_all = pd.concat([df_ratio, Features_col_all], axis=1)
    Features_col_all = pd.concat([df_acid, Features_col_all], axis=1)
    Features_col_all = pd.concat([df_brix, Features_col_all], axis=1)
    Features_col_all = pd.concat([df_number, Features_col_all], axis=1)
    Features_col_all.to_csv(path_save_file, index=False, header=True, na_rep='Unknown')

    return Features_col_all
