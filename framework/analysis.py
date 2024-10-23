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
        pass_cnt = 0
        fail_test = list()
        for item in test_data:
            if self.compare_values(item['output'], item['code_output']):
                pass_cnt += 1
            else:
                # collect failure case
                fail_test.append(item)

        record = {
            "test_file_path": test_fp,
            "pass_cnt": pass_cnt,
            "total_cnt": len(test_data),
            "pass_rate": np.round(pass_cnt / len(test_data), 3),
            "fail_test": fail_test
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

        total_pass = int(self.df["pass_cnt"].sum())  # Convert to int
        total_test = int(self.df["total_cnt"].sum())  # Convert to int
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

        self.logger.info(f"Summary: {stat}, exported to {json_fp}")


    def compare_values(self, a, b):
        """
        Compare two values, handle the case when the values are numeric strings
        """
        try:
            a = float(a)
            b = float(b)
            return np.isclose(a, b, atol=1e-5)
        except:
            return a == b

