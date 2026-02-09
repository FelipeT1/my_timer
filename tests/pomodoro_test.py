import pytest
from my_timer.Pomodoro import Pomodoro 
from unittest.mock import Mock

class TestPomodoro:

    def test_listener(self):
        pomodoro = Pomodoro(tasks=list())
        pomodoro.task = Mock(name="task_mock")
        state = Mock(name="state_mock")
        attrs = {"name": "FOCUS"}
        state.configure_mock(**attrs)
        attrs = {
                "start.return_value":None,
                "stop.return_value":None,
                "resume.return_value":None,
                "pause.return_value":None,
                "update.return_value":state
                }
        pomodoro.task.configure_mock(**attrs)
        pomodoro._stop.set()
        pomodoro._listener()
        pomodoro.task.stop.assert_called_once()
