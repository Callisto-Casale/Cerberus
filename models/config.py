import os

class Config:
    BASE_DIR = os.path.dirname(__file__)
    TARGET_FILE = os.path.join(BASE_DIR, "..", "data", "targets.json")
    TARGET_FILE = os.path.abspath(TARGET_FILE)
