import pandas as pd


class ResultAnalyzer:
    def __init__(self, result_dir, n_shot):
        self.result_dir = result_dir
        self.n_shot = n_shot

        self.total_pass = 0
        self.total_test = 0

        self.summary = list()

    def add_record(self, test_fp, test_data):
        pass_ct = 0
        for inp, out, ans in test_data:
            if ans and ans == out:  # ans is not None
                pass_ct += 1
        self.total_pass += pass_ct
        self.total_test += len(test_data)

        record = {
            "test_fp": test_fp,
            "pass_ct": pass_ct,
            "total_ct": len(test_data),
            "test": test_data,
        }
        self.summary.append(record)

    def export(self):
        df = pd.DataFrame(self.summary)
        csv_fp = f"{self.result_dir}/result-{self.n_shot}-shot.csv"
        df.to_csv(csv_fp, index=False)

    def get_stat(self):
        return {
            "total_pass": self.total_pass,
            "total_test": self.total_test,
            "pass_rate": self.total_pass / self.total_test,
        }
