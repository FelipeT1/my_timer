from datetime import date
from threading import Thread
from .Task import Task
from .SoundPlayer import SoundPlayer

class Pomodoro:
    """ A pomodoro manages tasks and logs pomodoros in a .json file """
    def __init__(self, tasks: list[Task]) -> None:
       self.task = None
       self._tasks = iter(tasks)
       self._date = date.today().isoformat()
       self._input_thread = Thread(target=self._events)
       self._listener_thread = Thread(target=self._listener)

       # Sound
       #self._soundplayer = SoundPlayer()

       # Events
       self._pause = Event()
       self._stop = Event()
       self._resume = Event()

    def _set_task(self) -> Task:
        """ Sets the next task to be worked on """
        return next(self._tasks)

    def _events(self) -> None:
        """ Get user input and signals the corresponding event """
        e = input("p(pause) s(stop) r(resume): ").lower()
        match e:
            case e == "p":
                self._pause.set()
            case e == "r":
                self._resume.set()
            case e == "s":
                self._stop.set()

    def _listener(self) -> None:
        """ Listen to events and executes the appropiate action """
        if self._pause.is_set():
            self.task.pause()
            self._pause.clear()

        elif self._resume.is_set():
            self.task.resume()
            self._resume.clear()

    def run(self) -> None:
        """ Main thread for the pomodoro """
        self._set_task()
        self._input_thread.start()
        self._listener_thread.start() 

        while self._stop.is_set():
            pass
