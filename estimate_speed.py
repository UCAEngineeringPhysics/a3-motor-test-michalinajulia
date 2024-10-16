from machine import Pin, PWM, Timer
from time import sleep
import time

INA_LEFT = Pin(8, Pin.OUT)
INA_RIGHT = Pin(20, Pin.OUT)
INB_LEFT = Pin(9, Pin.OUT)
INB_RIGHT = Pin(21, Pin.OUT)

INA_LEFT.off()
INA_RIGHT.off()
INB_LEFT.off()
INB_RIGHT.off()

PWM_LEFT = PWM(Pin(7))
PWM_RIGHT = PWM(Pin(19))
PWM_LEFT.freq(1000)
PWM_RIGHT.freq(1000)

INA_LEFT.on()
INA_RIGHT.on()

PWM_LEFT.duty_u16(int(65025/2))
PWM_RIGHT.duty_u16(int(65025/2))
sleep(60)

INA_LEFT.off()
INA_RIGHT.off()

PWM_LEFT.duty_u16(0)
PWM_RIGHT.duty_u16(0)
