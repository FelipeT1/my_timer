from time import monotonic

class Timer:
    """ API to Handle time functions """
    def __init__(self, duration: float) -> None:
        self._start = None
        self._paused_instant = None
        self._paused_time = 0.0
        self._duration = duration
        self._running = False

    def start(self) -> None:
        """ Starts the timer """
        self._start = monotonic()
        self._running = True

    def pause(self) -> None:
        """ Pauses the timer """
        self._running = False
        self._paused_instant = monotonic()

    def progress(self) -> float:
        """ The progress made compared to the duration in % """
        return self.elapsed() * 100.0 / self._duration

    def resume(self) -> float:
        """ Resumes the timer """
        if self._running:
            return 
        self._running = True
        paused_time = monotonic() - self._paused_instant
        self._paused_time += paused_time

    def elapsed(self) -> float:
        """ Time passed since the start point """
        if not self._start:
            raise RuntimeError("timer has not been started")
        time_passed = monotonic() - self._start - self._paused_time
        return time_passed
    
    def paused_time(self):
        """ Returns total paused time """
        return self._paused_time

    def __str__(self):
        """ Duration in hours """
        return f"{self._duration // 3600}h"
