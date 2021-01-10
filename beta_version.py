# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 100  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_med = 300
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

i = 0
# OBS Denna är "OK" justera nästa ben oxå sen köra detta script fast för det benet, sen köra med båda bena samtidigt
print('Moving servo on channel 0 & 2, press Ctrl-C to quit...')
while i > 3:
    print("sleeping 2 sec")
    time.sleep(2)
    print("moving upper leg to min")
    pwm.set_pwm(0, 0, servo_min)
    pwm.set_pwm(2, 0, servo_min)
    time.sleep(2)
    print("moveing upper leg to med")
    pwm.set_pwm(0, 0, servo_med)
    pwm.set_pwm(2, 0, servo_med)
    time.sleep(2)
    print("moveing upper leg to max")
    pwm.set_pwm(0, 0, servo_max)
    pwm.set_pwm(2, 0, servo_max)
    time.sleep(2)
    i += 1
    print("it's" , i)


 

