import argparse

import numpy as np
import pandas as pd

import exchange_calendars as xcal

parser = argparse.ArgumentParser(
    prog="Add TA35 days",
    description="add TA35 trading days in TradeStation format",
    epilog="Written by Eliran Sabag",
)

parser.add_argument("input", help="CSV file to read")
parser.add_argument("output", help="CSV file to save")

args = parser.parse_args()
input_filename = args.input
output_filename = args.output


data = pd.read_csv(
    input_filename,
    dtype={
        "Date": str,
        "Time": str,
        "Open": float,
        "High": float,
        "Low": float,
        "Close": float,
        "Volume": float,
        "Down": float,
        "Up": float,
    },
)
data.index = pd.to_datetime(data.Date, format="%m/%d/%Y")
# data

xtae = xcal.get_calendar("XTAE")
xtae_sessions = xtae.sessions_in_range(data.index[0], data.index[-1])
# xtae_sessions

new_data = pd.DataFrame(index=np.union1d(data.index, xtae_sessions))
new_data.loc[data.index, data.columns] = data
new_data.ffill(inplace=True)
new_data.Date = new_data.index.strftime("%m/%d/%Y")
new_data.to_csv(output_filename, index=False)
