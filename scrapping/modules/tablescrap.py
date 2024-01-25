#!/usr/bin/python3
import requests
import pandas as pd

def import_html_table(url, table_index=0, table_limit=None):
    # Read HTML tables from the specified URL
    tables = pd.read_html(url)

    # Check if the specified table index is within the range of available tables
    if table_index < len(tables) and (table_limit is None or table_index <= table_limit):
        # Return the DataFrame corresponding to the specified table index
        return tables[table_index]
    else:
        # Print a message if the specified index is out of range
        print(f"Error: Table index {table_index} is out of range.")
        return None