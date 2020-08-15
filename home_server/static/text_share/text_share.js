function copyText() {
    let textField = document.getElementById("id_content");

    textField.select();

    document.execCommand("copy");

    textField.blur();
}

document.getElementById("id_content").addEventListener("click", clearText);

function clearText(event) {
    event.target.value = "";
}