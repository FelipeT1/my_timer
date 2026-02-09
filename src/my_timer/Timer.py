from time import monotonic
from .TimerState import TimerState

class Timer:
    """ API to Handle time functions """
    def __init__(self, duration: float) -> None:
        self._start = None
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

    def progress(self) -> float:
        """ The progress made compared to the duration """
        return min(self.elapsed() * 100.0 / self._duration, 100.0)

    def resume(self) -> None:
        """ Resumes the timer """
        if self._state != TimerState.PAUSED:
            return 
        self._state = TimerState.RUNNING
        paused_time = monotonic() - self._paused_instant
        self._paused_time += paused_time

    def elapsed(self) -> float:
        """ Time passed since the start point """
        if self._state == TimerState.STOPPED:
            raise RuntimeError("timer is stopped")
        time_passed = monotonic() - self._start - self._paused_time
        return time_passed

    def update(self) -> None:
        """ Register the progress made """
        if self._state != TimerState.RUNNING:
            return 
        time_passed = self.elapsed() 
        self._progress = min(time_passed * 100.0 / self._duration, 100.0)
        if self.is_finished():
            self._state = TimerState.FINISHED
    
    def is_finished(self) -> bool:
        """ Verify if the time passed is enough to end the timer """
        return self.progress() == 100.0 or self._state == TimerState.STOPPED
        
    def paused_time(self) -> float:
        """ Returns total paused time """
        return self._paused_time

    def current_state(self) -> str:
        """ The current timer state """
        return self._state.name

    def __str__(self) -> str:
        """ Duration in hours """
        return f"{self._duration // 3600}h"
