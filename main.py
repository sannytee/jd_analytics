import os
import psycopg2

from utils.table_functions import load_csv_to_table, create_tables


def main():
    """
    This function mimics an EL process. it loads all the csv files in the data directory into the database.
    :return: None
    """

    conn_string = f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} " \
                  f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"

    # Connect to the database
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    # create tables if they don't exist
    create_tables(cur, conn)

    # Loop through the csv files and load them into the database
    for (dir_path, dir_names, filenames) in os.walk('data'):
        for csv_file in filenames:
            if csv_file.endswith('.csv'):  # Only load csv files
                csv_file_path = os.sep.join([dir_path, csv_file])
                table_name = csv_file.split('.')[0]
                load_csv_to_table(cur, conn, csv_file_path, table_name)

    # close the connection
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
