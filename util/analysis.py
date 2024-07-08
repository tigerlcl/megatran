import numpy as np
import pandas as pd


class ResultAnalyzer:
    def __init__(self):
        self.df = None
        self.summary = list()

    def add_record(self, test_fp, test_data):
        pass_ct = 0
        for inp, out, ans in test_data:
            if ans and compare_values(ans, out):  # ans is not None
                pass_ct += 1

        record = {
            "test_fp": test_fp,
            "pass_ct": pass_ct,
            "total_ct": len(test_data),
            "pass_rate": np.round(pass_ct / len(test_data), 3),
            "test": test_data,
        }
        self.summary.append(record)

    def export(self, csv_fp):
        self.df.to_csv(csv_fp, index=False)

    def to_df(self):
        self.df = pd.DataFrame(self.summary)

    def get_stat(self):
        return {
            "total_pass": self.df["pass_ct"].sum(),
            "total_test": self.df["total_ct"].sum(),
            "prate_per_sample": np.round(np.mean(self.df["pass_rate"]), 3),
            "prate_per_test": np.round(self.df["pass_ct"].sum() / self.df["total_ct"].sum(), 3)
        }


def compare_values(a, b, tolerance=1e-6):
    # try cast to float
    try:
        a = float(a)
        b = float(b)
        return abs(a - b) < tolerance
    except ValueError:
        return a == b
