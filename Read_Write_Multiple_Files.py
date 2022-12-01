import os
import sys
from Read_Logic import get_json_reader
from Write_Logic import load_db_table

def process_data(BASE_DIR, TABLE_NAME, conn):
    json_reader = get_json_reader(BASE_DIR, TABLE_NAME)
    for df in json_reader:
        load_db_table(df, conn, TABLE_NAME, df.columns[0])

def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    # TABLE_NAME = os.environ.get('TABLE_NAME')
    TABLE_NAME = sys.argv[1].split(",")
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    for name in TABLE_NAME:
        process_data(BASE_DIR, name, conn)

if __name__ == '__main__':
    main()