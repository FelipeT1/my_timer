import os 
from time import sleep
from datetime import date
from threading import Thread, Event
from .Task import Task
from .SoundPlayer import SoundPlayer

class Pomodoro:
    """ A pomodoro manages tasks and logs pomodoros in a .json file """
    def __init__(self, tasks: list[Task]) -> None:
       self.task = None
       self._tasks = iter(tasks)
       self._date = date.today().isoformat()
       self._input_thread = Thread(target=self._events, daemon=True)

       # OS
       self._os = 'unix'

       # TODO: has a progress bar

       # TODO: has a soundplayer
       #self._soundplayer = SoundPlayer()

       # Events
       self._pause = Event()
       self._stop = Event()
       self._resume = Event()
    
    def _set_task(self) -> None:
        """ Sets the next task to be worked on """
        try:
            self.task = next(self._tasks)
            self.task.start()
        except StopIteration as e:
            self._stop.set()

    def _events(self) -> None:
        """ Get user input and signals the corresponding event """
        while not self._stop.is_set():
            e = input().strip().lower()
            if e not in ["p", "r", "stop"]:
                print("Invalid input. Try again.")
                continue
            match e:
                case "p":
                    self._pause.set()
                case "r":
                    self._resume.set()
                case "stop":
                    self._stop.set()

    def _listener(self) -> None:
        """ Listen to events and executes the appropiate action """
        if self._pause.is_set():
            self.task.pause()
            self._pause.clear()

        elif self._resume.is_set():
            self.task.resume()
            self._resume.clear()

        elif self._stop.is_set():
            self.task.stop()
            self._stop.clear()

    def run(self) -> None:
        """ Main thread for the pomodoro """
        self._set_task()
        self._input_thread.start()
        while not self._stop.is_set():
            self._listener()
            state = self.task.update()
            os.system('clear')
            print(self.task, flush=True)
            print("p(pause) stop(stop) r(resume):",end=' ', flush=True)
            if state.name == "REST":
                self.task.start()
            if state.name == "FINISHED": 
                self._set_task()
            sleep(1)

    # TODO: Serialize
