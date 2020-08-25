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