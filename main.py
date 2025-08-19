from logic.watchdog.watchdog import Watchdog
from logic.chronos.chronos import Chronos
from multiprocessing import freeze_support

Watchdog()
chronos = Chronos()

if __name__ == "__main__":
    freeze_support()
    Chronos().run()