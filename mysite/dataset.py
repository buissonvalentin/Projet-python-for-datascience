import pandas as pd

main_folder = "../HAPT Data Set"
test_folder = f"{main_folder}/Test"
train_folder = f"{main_folder}/Train"

features_file = f"{main_folder}/features.txt"
activity_label_file = f"{main_folder}/activity_labels.txt"

X_train_file = f"{train_folder}/X_train.txt"
Y_train_file = f"{train_folder}/y_train.txt"
subject_Id_train_file = f"{train_folder}/subject_id_train.txt"

X_test_file = f"{test_folder}/X_test.txt"
Y_test_file = f"{test_folder}/y_test.txt"
subject_Id_test_file = f"{test_folder}/subject_id_test.txt"

#correct duplicated columns name
def correct_duplicated_columns_name(features):
    all_col = []
    multiple_col = []
    dic = {}
    for c in features:
        if c in all_col:
            multiple_col.append(c)
            dic[c] = 1
        all_col.append(c)

    new_names = []
    for c in features:
        if c in multiple_col:
            temp = f"{c[:-1]}{dic[c]}"
            dic[c] = dic[c] + 1
            new_names.append(temp)
        else:
            new_names.append(c)

    return new_names

#convert to float 
def convert_columns_to_float(df):
    for c in df.columns:
        if c not in ["label", "users_id"]:
            df[c] = [float(x) for x in df[c]]
    return df

from os import listdir
def read_df(train):
    df_file = X_train_file if train else X_test_file
    df = pd.read_csv(df_file, sep=" ", header=None)
    
    
    df_labels_file = Y_train_file if train else Y_test_file
    df_labels = pd.read_csv(df_labels_file, sep="\n", header=None)
    labels = list(df_labels[0].values)
    
    df_users_id_file = subject_Id_train_file if train else subject_Id_test_file
    df_users_id = pd.read_csv(df_users_id_file, sep="\n", header=None)
    users_id = list(df_users_id[0].values)
    
    
    df["users_id"] = users_id

    df["label"] = labels

    df.columns = get_features()

    df = convert_columns_to_float(df)
    
    print(df_file, df_labels_file, df_users_id_file)
    
    return df


def get_features():
    df_features = pd.read_csv(features_file, sep="\n", header=None)
    features = list(df_features[0].values)
    features = [x.strip() for x in features]
    features = correct_duplicated_columns_name(features)
    features.extend(["users_id", "label"])
    return features