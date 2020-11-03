import csv


def read(filename, in_label, out_label):
    d = {}
    with open(filename, "r") as file:
        r = csv.DictReader(file)
        for row in r:
            state = row.get("state")
            if state not in d:
                d[state] = {}
            cand = row.get("candidate_name")
            if cand not in d[state]:
                d[state][cand] = {}
            d[state][cand][out_label] = row[in_label]
    return d


def read_stdev():
    return read("./data/output/stdev_by_state.csv", "pct_trend_adjusted", "stdev")


def read_avg():
    return read("data/output/avg_by_state.csv", "pct_trend_adjusted", "avg")
