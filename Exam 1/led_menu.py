import led


def main():
    arduino = led.LED()
    arduino.connect()
    try:
        print("Serial Menu")
        print("0. Exit")
        print("1. LED ON")
        print("2. LED OFF")
        print("3. FLASH")
        while True:
            selection = int(input("Selection: "))
            if selection == 0:
                break
            elif selection == 1:
                arduino.send_command("LED ON")
            elif selection == 2:
                arduino.send_command("LED OFF")
            elif selection == 3:
                flashes = int(input("Number of flashes: "))
                period_ms = int(input("Period (ms): "))
                arduino.send_command("FLASH " + str(flashes) + " " + str(period_ms))
    finally:
        arduino.disconnect()
    print("Goodbye")


if __name__ == "__main__":
    main()
