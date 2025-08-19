# logic/chronos/chronos.py
import time
from logic.processes import base_processes as bp, running_processes as rp

class Chronos:
    def __init__(self):
        now = time.monotonic()
        self._next = {t.name: now for t in bp}

    def _clone(self, base):
        return base.__class__(
            name=base.name,
            target=base.target,
            frequency=base.frequency,
            SHOW_OUTPUT=base.SHOW_OUTPUT,
        )

    def run(self, tick: float = 0.2):
        while True:
            now = time.monotonic()
            for base in bp:
                freq = int(getattr(base, "frequency", 0) or 0)
                if freq <= 0:
                    continue
                if now >= self._next[base.name]:
                    child = self._clone(base)
                    child.start()
                    rp.put(child)
                    self._next[base.name] = now + freq
            time.sleep(tick)
