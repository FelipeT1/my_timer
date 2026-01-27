import pytest
from my_timer.Timer import Timer
from my_timer.TimerState import TimerState

class TestTimer:

    def test_start(self):
        t = Timer(100.0)
        t.start()
        assert t._state == TimerState.RUNNING 

    def test_update(self, monkeypatch):
        t = 100.0
        def monotonic():
            return t
        monkeypatch.setattr("my_timer.Timer.monotonic", monotonic)
        timer = Timer(100.0)
        timer.start()
        t = 200.0
        timer.update()
        assert timer._state == TimerState.FINISHED
    
    def test_progress(self, monkeypatch):
        t = 100.0
        def monotonic():
            return t
        monkeypatch.setattr("my_timer.Timer.monotonic", monotonic)
        timer = Timer(5.0)
        timer.start()
        t = 105.0
        assert timer.progress() == 100.0

    def test_elapsed(self, monkeypatch):
        t = 100.0
        def monotonic():
            return t
        monkeypatch.setattr("my_timer.Timer.monotonic", monotonic)
        timer = Timer(100.0)
        timer.start()
        t = 105.0
        assert timer.elapsed() == 5.0
    
    def test_elapsed_with_pause(self, monkeypatch):
        t = 100.0
        def monotonic():
            return t
        monkeypatch.setattr("my_timer.Timer.monotonic", monotonic)
        timer = Timer(100.0)
        timer.start()
        timer.pause()
        t = 105.0
        timer.resume()
        # 5s de pausa -> 110
        t = 110.0
        assert timer.elapsed() == 5.0
    
    def test_paused_time(self, monkeypatch):
        t = 100.0
        def monotonic():
            return t
        monkeypatch.setattr("my_timer.Timer.monotonic", monotonic)
        timer = Timer(100.0)
        timer.start()
        timer.pause()
        t = 200.0
        timer.resume()
        assert timer.paused_time() == 100.0
