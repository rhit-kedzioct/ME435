import serial
import time


class LED:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = port
        self.ser = None

    def connect(self):
        self.ser = serial.Serial(port=self.port, baudrate=19200, timeout=15)
        time.sleep(2)
        self.ser.reset_input_buffer()

    def disconnect(self):
        self.ser.close()

    def send_command(self, command):
        message_bytes = (command + "\n").encode()
        print(message_bytes)
        self.ser.write(message_bytes)
        response_bytes = self.ser.readline()
        response = response_bytes.decode().strip()
        print(response)
        return response


if __name__ == "__main__":
    print("Quick LED testing")
    led = LED()
    led.connect()
    try:
        response = led.send_command("LED ON")
        print("Response:", response)
    finally:
        led.disconnect()
