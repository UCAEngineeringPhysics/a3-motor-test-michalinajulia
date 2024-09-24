from machine import Pin, PWM
from time import sleep

# Motor control pins
INA1 = Pin(8, Pin.OUT)  # Motor 1 direction pin 1
INA2 = Pin(20, Pin.OUT)  # Motor 1 direction pin 2
INB1 = Pin(9, Pin.OUT)  # Motor 2 direction pin 1
INB2 = Pin(21, Pin.OUT)  # Motor 2 direction pin 2

# PWM setup
motor1_pwm = PWM(Pin(7), freq=1000)  # Adjust pin number as necessary
motor2_pwm = PWM(Pin(19), freq=1000)  # Adjust pin number as necessary
    
#     for _ in range(int(duration * 10)):
#         current_duty += step
#         if current_duty < 0:
#             current_duty = 0
#         elif current_duty > 65535:
#             current_duty = 65535
#         motor_pwm.duty_u16(int(current_duty))  # Update the PWM signal
#         sleep(0.1)

# Function to set motor direction and speed
def set_motor_forward(motor_pwm, INA, INB, speed):
    INA.value(1)  # Set direction to forward
    INB.value(0)  # Set opposite pin low
    motor_pwm.duty_u16(speed)  # Ensure the motor is stopped initially

def set_motor_backward(motor_pwm, INA, INB, speed):
    INA.value(0)  # Set direction to backward
    INB.value(1)  # Set opposite pin high
    motor_pwm.duty_u16(speed)  # Ensure the motor is stopped initially

# Ramp up both motors' speed forward in 4 seconds
for duty in range(100):
    set_motor_forward(motor1_pwm, INA1, INB1, int(62025*duty/100))
    set_motor_forward(motor2_pwm, INA2, INB2, int(62025*duty/100))
    sleep(4/100)
    

for duty in reversed(range(100)):
    set_motor_forward(motor1_pwm, INA1, INB1, int(62025*duty/100))
    set_motor_forward(motor2_pwm, INA2, INB2, int(62025*duty/100))
    sleep(4/100)


# Stop both motors
motor1_pwm.duty_u16(0)
motor2_pwm.duty_u16(0)
INA1.value(0)
INA2.value(0)
INB1.value(0)
INB2.value(0)

# Ramp up both motors' speed backward in 4 seconds
for duty in range(100):
    set_motor_backward(motor1_pwm, INA1, INB1, int(62025*duty/100))
    set_motor_backward(motor2_pwm, INA2, INB2, int(62025*duty/100))
    sleep(4/100)
    

for duty in reversed(range(100)):
    set_motor_backward(motor1_pwm, INA1, INB1, int(62025*duty/100))
    set_motor_backward(motor2_pwm, INA2, INB2, int(62025*duty/100))
    sleep(4/100)





# Stop both motors
motor1_pwm.duty_u16(0)
motor2_pwm.duty_u16(0)
INA1.value(0)
INA2.value(0)
INB1.value(0)
INB2.value(0)

# Cleanup
motor1_pwm.deinit()
motor2_pwm.deinit()
