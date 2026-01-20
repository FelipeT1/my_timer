from time import monotonic
from .TimeFormat import TimeFormat
from .TimerState import TimerState

class Timer:
    """ API to Handle time functions """
    def __init__(self, duration: float) -> None:
        self._start = None
        self._paused_instant = None
        self._paused_time = 0.0
        self._duration = TimeFormat.parse(duration) 
        self._state = TimerState()
        self.progress = 0.0

    def start(self) -> None:
        """ Starts the timer """
        self._start = monotonic()
        self._running = True

    def pause(self) -> None:
        """ Pauses the timer """
        self._state = TimerState.PAUSED
        self._paused_instant = monotonic()

    def progress(self, time_passed) -> None:
        """ The progress made compared to the duration in % """
        self._progress = time_passed * 100.0 / self._duration

    def resume(self) -> float:
        """ Resumes the timer """
        if self._state != TimerState.RUNNING:
            return 
        self._state = TimerState.RUNNING
        paused_time = monotonic() - self._paused_instant
        self._paused_time += paused_time

    def elapsed(self) -> float:
        """ Time passed since the start point """
        if not self._start:
            raise RuntimeError("timer has not been started")
        time_passed = monotonic() - self._start - self._paused_time
        self.progress(time_passed)
        return time_passed
    
    def paused_time(self):
        """ Returns total paused time """
        return self._paused_time

    def __str__(self):
        """ Duration in hours """
        return f"{self._duration // 3600}h"
