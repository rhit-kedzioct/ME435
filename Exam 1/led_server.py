import flask
import led
import threading


app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
arduino = led.LED()


@app.route("/")
def handle_naked_domain():
    return "Server is running"


@app.get("/api/led/<command>")
def handle_led_commands(command):
    with serial_lock:
        response = arduino.send_command("LED " + command.upper())
    return response


@app.get("/api/flash/<int:flashes>/<int:period_ms>")
def handle_flash(flashes, period_ms):
    with serial_lock:
        response = arduino.send_command("FLASH " + str(flashes) + " " + str(period_ms))
    return response


if __name__ == "__main__":
    print("Running flask!")
    arduino.connect()
    try:
        app.run(host="0.0.0.0", port=8080, use_reloader=False)
    finally:
        arduino.disconnect()
