import flask
import led
import threading


app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
arduino = led.LED()


@app.route("/")
def handle_naked_domain():
    return "LED server is running. Try /api/led/on, /api/led/off, or /api/flash/3/1000"


@app.get("/api/led/<command>")
def handle_led_commands(command):
    if command not in ("on", "off"):
        return "Unknown LED command", 404
    with serial_lock:
        try:
            response = arduino.send_command("LED " + command.upper())
        except TimeoutError as error:
            return str(error), 504
    return response, 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.get("/api/flash/<int:flashes>/<int:period_ms>")
def handle_flash(flashes, period_ms):
    if flashes <= 0 or period_ms <= 0:
        return "Flashes and period must be positive", 400
    with serial_lock:
        try:
            response = arduino.send_command("FLASH " + str(flashes) + " " + str(period_ms))
        except TimeoutError as error:
            return str(error), 504
    return response, 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    print("Running flask!")
    arduino.connect()
    try:
        app.run(host="0.0.0.0", port=5000, use_reloader=False)
    finally:
        arduino.disconnect()
