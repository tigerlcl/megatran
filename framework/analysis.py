import os
import json
import numpy as np
import pandas as pd


class ResultAnalyzer:
    def __init__(self, ctx):
        self.result_dir = ctx.result_dir
        self.logger = ctx.logger
        self.summary = list() # dataset-level summary

    def add_record(self, test_fp, test_data):
        pass_ct = 0
        for item in test_data:
            if 'code_output' in item and compare_values(item['output'], item['code_output']):  # ans is not None
                pass_ct += 1

        record = {
            "test_fp": test_fp,
            "pass_ct": pass_ct,
            "total_ct": len(test_data),
            "pass_rate": np.round(pass_ct / len(test_data), 3),
            "test": test_data,
        }
        self.summary.append(record)

    def export_csv_full_result(self):
        csv_fp = os.path.join(self.result_dir, 'full_result.csv')
        self.df = pd.DataFrame(self.summary)
        self.df.to_csv(csv_fp, index=False)
        self.logger.info(f"Full result exported to {csv_fp}")

    
    def export_json_summary(self):
        if self.df is None:
            self.df = pd.DataFrame(self.summary)

        total_pass = int(self.df["pass_ct"].sum())  # Convert to int
        total_test = int(self.df["total_ct"].sum())  # Convert to int
        prate_per_test = np.round(total_pass / total_test, 3)

        total_test_case = self.df.shape[0]
        total_pass_case = int(self.df[self.df["pass_rate"] == 1].shape[0])  # Convert to int
        prate_per_case = np.round(total_pass_case / total_test_case, 3) 

        stat =  {
            "total_pass": total_pass,
            "total_test": total_test,
            "prate_per_test": prate_per_test,
            "total_test_case": total_test_case,
            "total_pass_case": total_pass_case,
            "prate_per_case": prate_per_case 
        }

        json_fp = os.path.join(self.result_dir, 'summary.json')
        with open(json_fp, 'w') as f:
            json.dump(stat, f, indent=4)


def compare_values(a, b):
    if type(a) != type(b):
        return False
    
    if isinstance(a, (int, float, str)):
        return abs(a - b) < 1e-5 if isinstance(a, float) and isinstance(b, float) else a == b
    elif isinstance(a, list):
        return len(a) == len(b) and all(compare_values(x, y) for x, y in zip(a, b))
    elif isinstance(a, dict):
        return a.keys() == b.keys() and all(compare_values(a[k], b[k]) for k in a)
    
    return False  # For unsupported types, return False

