import multiprocessing as mp
import subprocess as sp
import sys

class Trace(mp.Process):
    def __init__(self, name, target, frequency, SHOW_OUTPUT):
        self.target = self.format_target_value(target)
        self.frequency = int(frequency)
        self.SHOW_OUTPUT = bool(SHOW_OUTPUT)
        super().__init__(name=name)

    def format_target_value(self, target):
        if isinstance(target, (list, tuple)):
            return [str(x) for x in target]
        elif isinstance(target, str):
            return [sys.executable, target]
        else:
            raise TypeError(f"Unsupported target type: {type(target).__name__}")

    def run(self):
        try:
            res = sp.run(self.target, capture_output=True, text=True, check=True)
            if self.SHOW_OUTPUT and res.stdout:
                print(res.stdout, end="")
        except sp.CalledProcessError as e:
            if self.SHOW_OUTPUT and e.stderr:
                print(e.stderr, end="")

    def get_all_info(self):
        return {
            "name": self.name,
            "target": self.target,
            "frequency": self.frequency,
            "SHOW_OUTPUT": self.SHOW_OUTPUT
        }
