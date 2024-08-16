import time

def pomodoroTimer(workMinutes, breakMinutes, cycles):
    """Run a Pomodoro timer for a given number of cycles."""
    for i in range(cycles):
        print(f"Work for {workMinutes} minutes.")
        time.sleep(workMinutes * 60)
        print(f"Break for {breakMinutes} minutes.")
        time.sleep(breakMinutes * 60)
    print("Pomodoro session complete!")

workMinutes = 25
breakMinutes = 5
cycles = 4
pomodoroTimer(workMinutes, breakMinutes, cycles)
