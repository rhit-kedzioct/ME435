import serial
import time


class PlateLoader:
    def __init__(self,port="/dev/ttyACM0"):
        self.port=port
        self.ser=None

    def connect(self):
        self.ser=serial.Serial(port=self.port, baudrate=19200,timeout=15)
        time.sleep(2)
        self.ser.reset_input_buffer()

    def disconnect(self):
        self.ser.close()

    def send_command(self, command):
        message_bytes=(command+"\n").encode()
        print(message_bytes)
        self.ser.write(message_bytes)
        response_bytes=self.ser.readline()
        print(response_bytes)
        response=response_bytes.decode().strip()
        print(response)

        return response

if __name__ == "__main__":
    print("Quick PlateLoader testing")
    loader=PlateLoader()
    loader.connect()
    reponse=loader.send_command("RESET")
    print("Response:", reponse)
    loader.disconnect()
