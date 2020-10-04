let textUpdateTime = null;
let socket = null

window.onload = function (){
    setTextUpdateTime();

    setInterval(updateTextAge, 60000);

    connectToServerSocket();
}

function copyText() {
    let textField = document.getElementById("id_content");

    textField.select();

    document.execCommand("copy");

    textField.blur();
}

document.getElementById("id_content").addEventListener("click", clearText);

function clearText(event) {
    let textField = document.getElementById("id_content");
    textField.innerHTML = "";
}

function refreshText() {
    $.ajax({
        url: refreshTextUrl,
        type: "GET",
        data: {},
        dataType: "json",
        success: function (data){
            let textField = document.getElementById("id_content");
            textField.innerHTML = data.text;
            console.log(data.text);
        },
        error: function (response){
            alert(response.statusText);
        }
    });
}

function setTextUpdateTime() {
    let date = new Date();
    textUpdateTime = date.getTime();
}

function updateTextAge() {
    let now = new Date();
    now = now.getTime();

    let age = now - textUpdateTime;
    age /= 1000;

    let ageText = "";
    let color = "";

    if (age <= 30) {
        ageText = "Just now";
        color = "green";
    }
    else if (age <= 60) {
        ageText = "Less than 1 min ago";
        color = "green";
    }
    else if (age <= 300) {
        ageText = "Less than 5 min ago";
        color = "red";
    }
    else if (age <= 3600) {
        ageText = "Less than 1 hour ago";
        color = "red";
    }
    else {
        ageText = "Long time ago";
        color = "red";
    }

    document.getElementById("textAge").innerText = ageText;
    document.getElementById("textAge").style.color = color;
}

function connectToServerSocket() {
    socket = new WebSocket("ws://" + "192.168.0.13" + ":" + "1234");

    console.log("Connected!");

    socket.onmessage = function (event){
        let text_field = document.getElementById("id_content");
        text_field.innerHTML = event.data;
        textUpdateTime = new Date().getTime();
        updateTextAge();
    }
}