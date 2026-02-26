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

    def elapsed(self) -> float:
        """ Time passed since the start """
        if self._state == TaskState.FOCUS:
            return self._focus.elapsed()

        elif self._state == TaskState.REST: 
            return self._rest.elapsed()

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
        if self._state == TaskState.FOCUS:
            return self._focus.current_state()

        else:
            return self._rest.current_state()

    def update(self) -> TaskState:
        """ Updates the task phase """
        if self.is_finished():
            if self._state == TaskState.FOCUS:
                self._state = TaskState.REST
            else:
                self._state = TaskState.FINISHED
        return self._state

    def __str__(self) -> str:
        if self._state == TaskState.FOCUS:
            return f"Task: {self._name} | Duration:{self._focus} | Timer: {self.timer_state()}"

        else:
            return f"Task: {self._name} | Duration:{self._rest} | Timer: {self.timer_state()}"
