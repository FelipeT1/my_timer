from .Task import Task

class Session:
    def __init__(self, tasks: list[Task]) -> None:
       self.tasks = tasks
