import math
from time import monotonic
from .TimerState import TimerState
from shutil import get_terminal_size

class Timer:
    """ API to Handle time functions """
    def __init__(self, duration: float) -> None:
        self._start = 0.0
        self._paused_instant = None
        self._paused_time = 0.0
        self._duration = duration 
        self._state = TimerState.STOPPED
        self._progress = 0.0

    def start(self) -> None:
        """ Starts the timer """
        if self._state != TimerState.STOPPED:
            return
        self._start = monotonic()
        self._state = TimerState.RUNNING

    def pause(self) -> None:
        """ Pauses the timer """
        if self._state != TimerState.RUNNING:
            return 
        self._state = TimerState.PAUSED
        self._paused_instant = monotonic()

    def stop(self) -> None:
        """ Stops the timer """
        self._state = TimerState.STOPPED

    def resume(self) -> None:
        """ Resumes the timer """
        if self._state != TimerState.PAUSED:
            return 
        self._state = TimerState.RUNNING
        paused_time = monotonic() - self._paused_instant
        self._paused_time += paused_time

    def _elapsed(self) -> float:
        """ Time passed since the start point """
        time_passed = monotonic() - self._start - self._paused_time
        return time_passed

    def progress(self) -> float:
        """ The progress made compared to the duration """
        time_passed = self._elapsed() 
        self._progress = min(time_passed * 100.0 / self._duration, 100.0)
        return self._progress

    def progress_bar(self) -> str:
        # Window size
        # returns a string of '#' based on the progress made
        width, height = get_terminal_size()
        n = math.floor(((width * 1/4) * self._progress) / 100)
        return n * '#'

    def is_finished(self) -> bool:
        """ Verify if the time passed is enough to end the timer """
        return self._progress == 100.0 or self._state == TimerState.STOPPED
        
    def paused_time(self) -> float:
        """ Returns total paused time """
        return self._paused_time

    def current_state(self) -> str:
        """ The current timer state """
        return self._state.name

    def update(self) -> None:
        """ Register the progress made """
        if self._state != TimerState.RUNNING:
            return 
        self.progress()
        if self.is_finished():
            self._state = TimerState.FINISHED
    
    def __str__(self) -> str:
        """ Duration in hours """
        return f"{self._duration / 3600}h"
