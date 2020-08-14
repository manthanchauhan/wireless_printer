function copyText() {
    let textField = document.getElementById("id_content");

    textField.select();

    document.execCommand("copy");

    textField.blur();

}
