import gpiozero as gz
import time
import signal

def sequence_repeater():
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)
    button_red = gz.Button(22)
    button_yellow = gz.Button(23)
    button_green = gz.Button(24)
    button_repeat = gz.Button(25)
    sequence = []

    def repeat_sequence():
        for i in range(len(sequence)):
            sequence[i].on()
            time.sleep(0.5)
            sequence[i].off()
            if i < len(sequence) - 1:
                time.sleep(0.1)
        sequence.clear()
    button_red.when_pressed = lambda: (red_led.on(), sequence.append(red_led))
    button_red.when_released = lambda: red_led.off()
    button_yellow.when_pressed = lambda: (yellow_led.on(), sequence.append(yellow_led))
    button_yellow.when_released = lambda: yellow_led.off()
    button_green.when_pressed = lambda: (green_led.on(), sequence.append(green_led))
    button_green.when_released = lambda: green_led.off()
    button_repeat.when_pressed = lambda: repeat_sequence()
    signal.pause()

def main():
    sequence_repeater()

main()