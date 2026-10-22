import gpiozero as gz
import time
import signal

def basic_on_off():
    print("b")
    green_led=gz.DigitalOutputDevice(18)
    green_led.on()
    time.sleep(3)
    green_led.off()

def fancy_leds():
    print("f")
    red_led=gz.LED(14)
    yellow_led=gz.LED(15)
    green_led=gz.LED(18)

    # yellow_led.blink(on_time=2, off_time=0.1, n=3, background=False)
    yellow_led.blink(on_time=2, off_time=0.1)
    time.sleep(.1)
    red_led.blink(on_time=2, off_time=0.1)
    time.sleep(.1)
    green_led.blink(on_time=2, off_time=0.1)
    signal.pause()

def led_board():
    board=gz.LEDBoard(14, 15,18, pwm=True)
    board.value=(1,0,1)
    time.sleep(1)
    board.value=(0,0.5,0)
    time.sleep(1)
    # for k in range(5):
    #     board.on()
    #     time.sleep(1)
    #     board.off()
    #     time.sleep(1)
    #     board.red.on()
    #     board.green.on()
    #     time.sleep(1)



    

def main():
    print("Leds")
    led_board()

main()
