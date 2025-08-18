import multiprocessing as mp
import subprocess as sp
import sys

class Trace(mp.Process):
    def __init__(self, name, target, SHOW_OUTPUT=False):
        self.target = self.format_target_value(target)
        self.SHOW_OUTPUT=SHOW_OUTPUT
        super().__init__(name=name)

    def format_target_value(self, target):
        return [sys.executable, target]

    def run(self):
        result = sp.check_output(self.target)
        if self.SHOW_OUTPUT:
            print(result)
