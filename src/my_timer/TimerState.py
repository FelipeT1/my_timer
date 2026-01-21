from enum import Enum, auto

class TimerState(Enum):
    RUNNING = auto()
    PAUSED = auto()
    STOPPED = auto()
    FINISHED = auto()
