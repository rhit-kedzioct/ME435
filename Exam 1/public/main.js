
function ledOn() {
    fetch("/api/led/on")
        .then(response => response.text())
        .then(data => {
            document.getElementById("response").innerText = data;
        })
        .catch(error => {
            document.getElementById("response").innerText = "Error: " + error;
        });
}

function ledOff() {
    fetch("/api/led/off")
        .then(response => response.text())
        .then(data => {
            document.getElementById("response").innerText = data;
        })
        .catch(error => {
            document.getElementById("response").innerText = "Error: " + error;
        });
}

function flashLed() {
    let flashes = document.getElementById("flashes").value;
    let period = document.getElementById("period").value;

    if (flashes <= 0 || period <= 0 || !Number.isInteger(Number(flashes)) || !Number.isInteger(Number(period))) {
        document.getElementById("response").innerText = "Please enter positive whole numbers.";
        return;
    }

    fetch("/api/flash/" + flashes + "/" + period)
        .then(response => response.text())
        .then(data => {
            document.getElementById("response").innerText = data;
        })
        .catch(error => {
            document.getElementById("response").innerText = "Error: " + error;
        });
}

function main() {
    console.log("Arduino LED Web App Ready!");
}

main();
