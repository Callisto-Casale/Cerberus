import multiprocessing as mp
import subprocess as sp
import sys

class Trace(mp.Process):
    def __init__(self, name, target, frequency, SHOW_OUTPUT):
        self.target = self.format_target_value(target)
        self.frequency = frequency
        self.SHOW_OUTPUT=SHOW_OUTPUT
        super().__init__(name=name)

    def format_target_value(self, target):
        return [sys.executable, target]

    def run(self):
        result = sp.check_output(self.target)
        if self.SHOW_OUTPUT:
            print(result)
    
    def get_all_info(self):
        return {
            "name": self.name,
            "target": self.target,
            "frequency": self.frequency,
            "SHOW_OUTPUT": self.SHOW_OUTPUT
        }
