import os
import pandas as pd

def get_json_reader(BASE_DIR, table_name, chunksize=1000):
    file_name = os.listdir(f'{BASE_DIR}\\{table_name}')[0]
    file_path = f'{BASE_DIR}\\{table_name}\\{file_name}'
    print('File path :', file_path)
    return pd.read_json(file_path, lines=True, chunksize=chunksize)

if __name__ == '__main__':
    BASE_DIR = os.environ.get("BASE_DIR")
    table_name = os.environ.get("TABLE_NAME")
    json_reader = get_json_reader(BASE_DIR, table_name)
    for idx, df in enumerate(json_reader):
        print(f'Number of records in chunks with {idx} is {df.shape[0]}')
