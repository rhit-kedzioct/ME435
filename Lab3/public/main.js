async function sendCommand(command){
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;
}

function main(){
    console.log("Hello JavaScrpit!")
    //document.querySelector("#reset").innerHTML = "Hello";
    document.querySelector("#reset").onclick = () => {
        console.log("You pressed a button!");
        sendCommand("RESET");

        document.querySelector("#move").onclick = () => {
            let moveFrom = document.querySelector("#moveFrom").value;
            let moveTo = document.querySelector("#moveTo").value;
            console.log(`MOVE ${moveFrom} ${moveTo}`);
            sendCommand(`MOVE ${moveFrom} ${moveTo}`);
        };


    };
}


main();
