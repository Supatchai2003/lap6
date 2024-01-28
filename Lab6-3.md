import RPi.GPIO as GPIO
import time
SW = 22
LED = 18
St = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
try:
    while True:
            if GPIO.wait_for_edge(SW, GPIO.FALLING):
                St = St+1
                if St%2 == 0:
                    GPIO.output (LED,True)
                    print("On")
                else :
                    GPIO.output (LED,False)
                    print("Off")
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye…")
