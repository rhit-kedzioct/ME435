async function sendCommand(command) {
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;
}

function main() {
    console.log("Exam 1");

    document.querySelector("#ledOn").onclick = () => {
        console.log("LED On pressed!");
        sendCommand("led/on");
    };

    document.querySelector("#ledOff").onclick = () => {
        console.log("LED Off pressed!");
        sendCommand("led/off");
    };

    document.querySelector("#flash").onclick = () => {
        let flashes = document.querySelector("#flashes").value;
        let period = document.querySelector("#period").value;

        console.log(`FLASH ${flashes} ${period}`);
        sendCommand(`flash/${flashes}/${period}`);
    };
}

main();