#!/usr/bin/python3
import requests
import pandas as pd
from scrapping.modules.tablescrap import import_html_table


def table_scrap(url, table_index=0, table_limit=None):
    while table_index <= table_limit:
        result_table = import_html_table(url, table_index)

        if result_table is not None:
            result_table.to_csv(f'file_{table_index}.csv', index=False)

        table_index += 1

if __name__ == "__main__":
    import sys

    tables = pd.read_html(sys.argv[1])

    if len(tables) > 0:
        limiter = len(tables)
    else:
        print("Error: No tables found in the provided URL.")
        sys.exit(1)

    if len(sys.argv) > 4:
        print("Usage: python main_script.py <url> <table_index> <table_limit>")
        sys.exit(1)

    if len(sys.argv) == 3:
        url = sys.argv[1]
        table_index = int(sys.argv[2])
        table_limit = limiter
        table_scrap(url, table_index, table_limit)

    else:
        url = sys.argv[1]
        table_index = int(sys.argv[2])
        table_limit = int(sys.argv[3])
        table_scrap(url, table_index, table_limit)

