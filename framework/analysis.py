import numpy as np
import pandas as pd
import json


class ResultAnalyzer:
    def __init__(self):
        self.df = None
        self.summary = list() # dataset-level summary

    def add_record(self, test_fp, test_data):
        pass_ct = 0
        for item in test_data:
            if item['code_output'] and compare_values(item['output'], item['code_output']):  # ans is not None
                pass_ct += 1

        record = {
            "test_fp": test_fp,
            "pass_ct": pass_ct,
            "total_ct": len(test_data),
            "pass_rate": np.round(pass_ct / len(test_data), 3),
            "test": test_data,
        }
        self.summary.append(record)

    def export_from_dataframe(self, csv_fp):
        self.df = pd.DataFrame(self.summary)
        self.df.to_csv(csv_fp, index=False)


    def get_stat(self):
        return {
            "total_pass": self.df["pass_ct"].sum(),
            "total_test": self.df["total_ct"].sum(),
            "prate_per_test": np.round(self.df["pass_ct"].sum() / self.df["total_ct"].sum(), 3),
            "total_test_case": self.df.shape[0],
            "total_pass_case": (self.df[self.df["pass_rate"] == 1].shape[0]),
            "prate_per_case": np.round((self.df[self.df["pass_rate"] == 1].shape[0]) / self.df.shape[0], 3) 
        }
    
    def export_stat(self, json_fp):
        with open(json_fp, 'w') as f:
            json.dump(self.get_stat(), f)


def compare_values(a, b, tolerance=1e-6):
    try: # try cast to float
        a = float(a)
        b = float(b)
        return abs(a - b) < tolerance
    except Exception:
        return a == b
