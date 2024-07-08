import re

API_TRIGGER = {
    "format()": "format the input data properly",
    "convert()": "convert the input data to the desired format",
    "regex()": "apply proper regex pattern to process"
}


class InstructionBuilder:
    def __init__(self, inst_fp, test_fp, n_shot):
        self.inst_fp = inst_fp
        self.test_fp = test_fp
        self.n_shot = n_shot

        self.inst_data = ""
        self.shot_data = ""
        self.test_data = list()

    # load expert instruction and parse the API trigger
    # TODO: integrate more APIs
    def __load_inst_data(self):
        with open(self.inst_fp, 'r') as f:
            for line in f.readlines():
                api_name, note = line.strip().split(':', maxsplit=1)
                if api_name in API_TRIGGER:
                    self.inst_data += f"{API_TRIGGER[api_name]}: {note}"
                else:
                    self.inst_data += f"{line}"

    def __load_test_data(self):
        with open(self.test_fp, 'r') as f:
            # preprocess func on TDE data only, need adapt other datasets
            _ = f.readline()  # skip header

            shot_count = 0
            while shot_count < self.n_shot:
                line = f.readline().strip().split('\t', maxsplit=1)
                if len(line) != 2:  # temp skip bad case, e.g. stackoverflow/2.txt
                    continue
                self.shot_data += f"input: {line[0]}, output: {line[1]}\n"
                shot_count += 1

            # the rest would bd the test data
            self.test_data = [re.split('\t+', line.strip()) for line in f.readlines()]

    def load_test_data(self):
        return self.test_data

    # run
    def run(self):
        self.__load_inst_data()
        self.__load_test_data()

        prompt = f"### Instruction ###\n{self.inst_data}\n\n### Examples ###\n{self.shot_data}"
        return prompt
