import RPi.GPIO as GPIO
import time

PIN_RED = 17
PIN_GREEN = 18
PIN_BLUE = 27
PIN_SWITCH = 22


COLOR_CHANGE_INTERVAL = 0.5


COLOR_MODES = [
    (0, 0, 0),  # Black
    (0, 0, 1),  # Blue
    (0, 1, 0),  # Green
    (0, 1, 1),  # Cyan
    (1, 0, 0),  # Red
    (1, 0, 1),  # Purple
    (1, 1, 0),  # Yellow
    (1, 1, 1),  # White
]


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)
GPIO.setup(PIN_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def change_color(color):
    GPIO.output(PIN_RED, color[0])
    GPIO.output(PIN_GREEN, color[1])
    GPIO.output(PIN_BLUE, color[2])

def main():
    color_index = 0

    try:
        while True:
            if GPIO.input(PIN_SWITCH) == GPIO.LOW:
                color_index = (color_index + 1) % len(COLOR_MODES)
                time.sleep(0.2)  
            change_color(COLOR_MODES[color_index])
            time.sleep(COLOR_CHANGE_INTERVAL)
    except KeyboardInterrupt:
        GPIO.cleanup()
    print('Bye')

if __name__ == "__main__":
    main()
