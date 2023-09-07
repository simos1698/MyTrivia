function tasia(url) {
    const xhttp = new XMLHttpRequest();
    const button = document.getElementById("test");
    
    xhttp.onload = function() {
        console.log(url)
        console.log(button.innerHTML);

        if(button.innerHTML == "Kaktos")
            button.innerHTML = "Tasia";
        else 
            button.innerHTML = "Kaktos";
        
    }

    xhttp.open("GET", url);
    xhttp.send();
}