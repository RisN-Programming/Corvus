import time

#GPIO initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Reed switches GPIO
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #reed 1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #reed 2
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #reed 3
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #reed 4

#LED for reed switch
GPIO.setup(26, GPIO.OUT)  #reed 1 tripped indicator
GPIO.setup(6, GPIO.OUT)   #reed 2 tripped indicator
GPIO.setup(23, GPIO.OUT)  #reed 3 tripped indicator
GPIO.setup(24, GPIO.OUT)  #reed 4 tripped indicator

running = True
while running:
    if GPIO.input(17) == GPIO.HIGH:
        GPIO.output(26,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(.5)

    if GPIO.input(27) == GPIO.HIGH:
        GPIO.output(6,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(6,GPIO.HIGH)
        time.sleep(.5)

    if GPIO.input(22) == GPIO.HIGH:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(.5)

    if GPIO.input(5) == GPIO.HIGH:
        GPIO.output(24,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(.5)
