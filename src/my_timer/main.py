from .Pomodoro import Pomodoro
from .Task import Task

def _create_task() -> Task:
    """ Create tasks for a Pomodoro """
    name = input("Task name: ")
    focus = input("Focus Timer(00h00m00s): ")
    rest = input("Rest Timer(00h00m00s): ")
    return Task(name, focus, rest)

def create_pomodoro() -> Pomodoro:
    """ Loops to create and append tasks to a list then returns a Pomodoro """
    tasks = list()
    while True:
        choice = input("Create task? y/n ").lower().strip()
        if choice in ['y', 'yes']:
            try:
                task = _create_task()
                tasks.append(task)
            except ValueError as e:
                print("Something went wrong. Try time format 00h00m00s")
                continue
        elif choice in ['n', 'no']:
            break
        else:
            continue
    return Pomodoro(tasks)

if __name__ == "__main__":
    pomodoro = create_pomodoro()
    pomodoro.run()
