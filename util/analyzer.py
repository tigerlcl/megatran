import os
import json
import numpy as np
import pandas as pd
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class TestRecord:
    test_file_path: str
    pass_cnt: int
    total_cnt: int
    pass_rate: float
    full_test: List[Dict[str, Any]]

@dataclass
class TokenUsage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    count: int  # number of API calls

    def add_usage(self, prompt_tokens: int, completion_tokens: int):
        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens
        self.total_tokens += (prompt_tokens + completion_tokens)
        self.count += 1

    @property
    def avg_usage(self) -> Dict[str, float]:
        if self.count == 0:
            return {"total_api_calls": 0, "avg_prompt": 0, "avg_completion": 0, "avg_total": 0}
        return {
            "total_api_calls": self.count, # include the number of API calls
            "avg_prompt": round(self.prompt_tokens / self.count, 2),
            "avg_completion": round(self.completion_tokens / self.count, 2),
            "avg_total": round(self.total_tokens / self.count, 2)
        }

class ResultAnalyzer:
    def __init__(self, result_dir):
        self.result_dir = result_dir
        self.summary: List[TestRecord] = []  # dataset-level summary
        
        # Token usage tracking per module
        self.token_usage = {
            "chat_to_inst": TokenUsage(0, 0, 0, 0),
            "code_generation": TokenUsage(0, 0, 0, 0),
            "reflection": TokenUsage(0, 0, 0, 0),
            "lazy_rag": TokenUsage(0, 0, 0, 0)
        }

    def compare_values(self, expected: Any, actual: Any) -> bool:
        """Compare two values after normalization"""
        try:
            expected = float(expected)
            actual = float(actual)
            return np.isclose(expected, actual, atol=1e-5)
        except:
            return expected == actual

    def add_record(self, test_fp: str, test_data: List[Dict[str, Any]]):
        """Add test record with improved value comparison"""
        pass_cnt = sum(1 for item in test_data 
                      if self.compare_values(item['output'], item['code_output']))
        
        record = TestRecord(
            test_file_path=test_fp,
            pass_cnt=pass_cnt,
            total_cnt=len(test_data),
            pass_rate=np.round(pass_cnt / len(test_data), 3),
            full_test=test_data
        )
        self.summary.append(record)

        return pass_cnt

    def add_token_usage(self, module: str, prompt_tokens: int, completion_tokens: int):
        """Track token usage for a specific module"""
        if module in self.token_usage:
            self.token_usage[module].add_usage(prompt_tokens, completion_tokens)

    def export_csv_full_result(self):
        """Export full test results to CSV"""
        csv_fp = os.path.join(self.result_dir, 'full_result.csv')
        summary_df = pd.DataFrame(self.summary)
        summary_df.to_csv(csv_fp, index=False)
        return csv_fp

    def export_json_summary(self):
        """Export summary statistics to JSON"""
        summary_df = pd.DataFrame(self.summary)

        total_pass = int(summary_df["pass_cnt"].sum())
        total_test = int(summary_df["total_cnt"].sum())
        prate_per_test = np.round(total_pass / total_test, 3)

        total_test_case = summary_df.shape[0]
        total_pass_case = int(summary_df[summary_df["pass_rate"] == 1].shape[0])
        prate_per_case = np.round(total_pass_case / total_test_case, 3) 

        # Include token usage in summary
        token_stats = {
            module: usage.avg_usage
            for module, usage in self.token_usage.items()
        }
        
        stat = {
            "test_summary": {
                "total_pass": total_pass,
                "total_test": total_test,
                "prate_per_test": prate_per_test,
                "total_task": total_test_case,
                "total_pass_task": total_pass_case,
                "prate_per_task": prate_per_case 
            },
            "token_usage": token_stats
        }

        json_fp = os.path.join(self.result_dir, 'summary.json')
        with open(json_fp, 'w') as f:
            json.dump(stat, f, indent=4)

        return json_fp
