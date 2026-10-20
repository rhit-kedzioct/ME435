import gpiozero as gz
import time
import signal

def button_state():
    buttton=gz.Button(25)

    while True:
        if buttton.is_pressed:
            print("Button is pressed")

        else:
            print("Button is not pressed")
        time.sleep(.5)

def function_using_def():
    print("this is function")

function_using_lambda=lambda: print("this is lambda function")

def some_helper_function(board,brightness):
    print("helper")
    board.value=(brightness,0,brightness)
    time.sleep(1)
    board.off()
    time.sleep(1)
    

def button_events():
    print("l")
    button=gz.Button(25)
    board=gz.LEDBoard(14, 15,18, pwm=True)

    button.when_pressed= function_using_def
    button.when_released= function_using_lambda
    button.when_held=lambda:some_helper_function(board,0.3)


    signal.pause()



def main():
    print("l")
    # button_state()
    button_events()


main()