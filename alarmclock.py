
from playsound import playsound 
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H]"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{minutes_left:02d}:{seconds_left:02d}")

    playsound("alarmsound.mp3")

# Setting alarm for 10 seconds
alarm(10)
