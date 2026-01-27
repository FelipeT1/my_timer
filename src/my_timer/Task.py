from time import sleep
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

    def start(self) -> None:
        """ Starts the timer for the current task """
        if self._state == TaskState.FOCUS:
            self._focus.start()

        elif self._state == TaskState.REST: 
            self._rest.start()

    def pause(self) -> None:
        """ Pauses the timer for the current task """
        if self._state == TaskState.FOCUS:
            self._focus.pause()

        elif self._state == TaskState.REST: 
            self._rest.pause()
    
    def stop(self) -> None:
        """ Stops the timer and returns the current progress """
        if self._state == TaskState.FOCUS:
            self._focus.stop()

        elif self._state == TaskState.REST: 
            self._rest.stop()

    def resume(self) -> None:
        """ Resumes a paused timer """
        if self._state == TaskState.FOCUS:
            self._focus.resume()

        elif self._state == TaskState.REST: 
            self._rest.resume()

    def progress(self) -> float:
        """ Returns the timer's progress for this task """
        if self._state == TaskState.FOCUS:
            return self._focus.progress()

        elif self._state == TaskState.REST: 
            return self._rest.progress()

    def elapsed(self) -> float:
        """ Time passed since the start """
        if self._state == TaskState.FOCUS:
            return self._focus.elapsed()

        elif self._state == TaskState.REST: 
            return self._rest.elapsed()

    def is_finished(self) -> bool:
        """ Verify is the timer is finished """
        if self._state == TaskState.FOCUS:
            return self._focus.is_finished()

        elif self._state == TaskState.REST: 
            return self._rest.is_finished()

    def update(self) -> None:
        """ Updates the task phase """
        if self.is_finished():
            if self._state == TaskPhase.FOCUS:
                self._state = TaskPhase.REST
            else:
                self._state = TaskPhase.FINISHED

    def __str__(self) -> str:
        if self._state == TaskState.FOCUS:
            return f"Task: {self._name}\nDuration:{self._focus}"

        elif self._state == TaskState.REST: 
            return f"Task: {self._name}\nDuration:{self._rest}"
