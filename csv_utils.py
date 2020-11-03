import csv


def read_stats_by_state_to_dict(filename, in_label, out_label):
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
            d[state][cand][out_label] = float(row[in_label])
    return d


def read_electoral_to_dict():
    d = {}
    with open("./data/electoral.csv", "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            d[row["state"]] = int(row["value"])
    return d


def read_array(filename):
    arr = []
    with open(filename, "r") as file:
        _reader = csv.reader(file)
        for row in _reader:
            arr += [row]
    return arr


def read_stdev():
    return read_stats_by_state_to_dict("./data/output/stdev_by_state.csv", "pct_trend_adjusted", "stdev")


def read_avg():
    return read_stats_by_state_to_dict("data/output/avg_by_state.csv", "pct_trend_adjusted", "avg")
