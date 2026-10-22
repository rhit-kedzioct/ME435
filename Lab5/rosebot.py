import gpiozero as gz
from rosebot_drive_system import DriveSystem

class RoseBot:
    def __init__(self):
        self.drive_system = DriveSystem()
        self.leds = LED()
        self.ultrasonic = Claw()
        self.line_sensors = LineSensors()
        self.servo_head = ServoHead()
        self.buzzer= gz.Buzzer(17)
        self.adc=None

