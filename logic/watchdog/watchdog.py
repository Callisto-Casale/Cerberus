from models.config import Config
from models.trace import Trace
from logic.processes import running_processes as rp
from logic.processes import base_processes as bp
import json

class Watchdog:
    def __init__(self):
        self.create_trace_from_targets()
        
    def create_trace_from_targets(self):
        with open(Config.TARGET_FILE, 'r') as fp:
            data = json.load(fp)
            
        for t in data:
            if not (
                isinstance(t.get("name"), str) and
                isinstance(t.get("target"), str) and
                isinstance(t.get("frequency"), int) and
                isinstance(t.get("SHOW_OUTPUT"), bool)
            ):
                continue

            new_t = Trace(
                t["name"], t["target"], t["frequency"], t["SHOW_OUTPUT"]
            )
            bp.append(new_t)