import pandas as pd
import numpy as np


def load_averages():
    _df = pd.read_csv("./data/forecasts/presidential_poll_averages_2020.csv")
    cols = ["modeldate", "state", "candidate_name", "pct_trend_adjusted"]
    return _df[cols]


def get_stdev() -> pd.DataFrame:
    _df = load_averages()
    _df = _df.groupby(["state", "candidate_name"])
    return _df.agg(np.std)


def get_avg() -> pd.DataFrame:
    _df = load_averages()
    _df = _df.groupby(["state", "candidate_name"])
    return _df.agg(np.average)


def to_csv():
    _df_s = get_stdev()
    _df_a = get_avg()
    _df_s.to_csv("./data/output/stdev_by_state.csv")
    _df_a.to_csv("./data/output/avg_by_state.csv")
