from .Timer import Timer
from .TimeFormat import TimeFormat
from .TaskState import TaskState

class Task:
    """ A task has a name and is composed of a focus and rest Timers """

    def __init__(self, name: str, focus_time: str, rest_time: str):
        self._name = name
        self._focus = Timer(TimeFormat.parse(focus_time))
        self._rest = Timer(TimeFormat.parse(rest_time))
        self._state = TaskState.FOCUS

    def _current_timer(self) -> Timer:
        """ Returns the timer being used by the task """
        if self._state == TaskState.FOCUS:
            return self._focus
        return self._rest

    def start(self) -> None:
        """ Starts the timer for the current task """
        self._current_timer().start()

    def pause(self) -> None:
        """ Pauses the timer for the current task """
        self._current_timer().pause()
    
    def stop(self) -> None:
        """ Stops the timer and returns the current progress """
        self._current_timer().stop()

    def resume(self) -> None:
        """ Resumes a paused timer """
        self._current_timer().resume()

    def elapsed(self) -> float:
        """ Time passed since the start """
        self._current_timer().elapsed()

    def is_finished(self) -> bool:
        """ Verify if the timer is finished """
        if self._state == TaskState.FOCUS:
            self._focus.update()
            return self._focus.is_finished()

        elif self._state == TaskState.REST: 
            self._rest.update()
            return self._rest.is_finished()

    def timer_state(self) -> bool:
        """ Get the timer state """
        self._current_timer().current_state()

    def update(self) -> TaskState:
        """ Updates the task phase """
        if self.is_finished():
            if self._state == TaskState.FOCUS:
                self._state = TaskState.REST
            else:
                self._state = TaskState.FINISHED
        return self._state

    def __str__(self) -> str:
        return f"Task: {self._name} - {self._state.name} | Timer: {self._current_timer().timer_state()}\n{self._current_timer().progress_bar()}"
