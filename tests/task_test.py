import pytest
from my_timer.Task import Task
from my_timer.TaskState import TaskState

class TestTask:

    def test_update(self, monkeypatch):
        t = 0.0
        def monotonic():
            return t
        monkeypatch.setattr("my_timer.Timer.monotonic", monotonic)
        task = Task("python", "1m40s", "10s")
        task.start()
        t = 100.0
        task.update()
        assert task._state == TaskState.REST
        


