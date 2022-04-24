function myFunction() {
    var copyText = document.getElementById("url");
    copyText.select();
    document.execCommand("Copy")
}