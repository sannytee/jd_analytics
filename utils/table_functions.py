

def create_tables(cur, conn) -> None:
    """
    Create the required tables if they don't exist
    :param cur:
    :param conn:
    :return: None
    """
    queries = [
        """
        CREATE TABLE IF NOT EXISTS adspend (
            event_date DATE,
            country_id int,
            network_id int,
            client_id int,
            value_usd float
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS installs (
            install_id VARCHAR,
            country_id int,
            app_id int,
            network_id int,
            event_date DATE,
            device_os_version VARCHAR
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS payouts (
            install_id VARCHAR,
            event_date DATE,
            value_usd float
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS revenue (
            install_id VARCHAR,
            event_date DATE,
            value_usd float
        )
        """
    ]
    for query in queries:
        cur.execute(query)
        conn.commit()


def load_csv_to_table(cur, conn, csv_file, table_name) -> None:
    """
    Load a csv file into a table
    :param conn:
    :param cur:
    :param csv_file:
    :param table_name:
    :return: None
    """
    with open(csv_file, 'r') as f:
        next(f)
        cur.copy_from(f, table_name, sep=',')
        conn.commit()
