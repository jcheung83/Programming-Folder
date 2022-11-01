var requests=4;
var connections=587;

function accept(element){
    if (requests>0)
        requests--;
    connections++;
    var numberOfRequests = document.querySelector("#numberOfRequests");
    numberOfRequests.innerText = requests;
    var numberOfConnections = document.querySelector("#numberOfConnections");
    numberOfConnections.innerText = connections;
    removeFadeOut(element, 500);
}

function removeFadeOut( el, speed ) {
    var seconds = speed/1000;
    el.style.transition = "opacity "+seconds+"s ease";
    el.style.opacity = 0;
    setTimeout(function() {
        el.remove();
    }, speed);
}

function refuse(element){
    if (requests>0)
        requests--;
    removeFadeOut(element, 500);
    var numberOfRequests = document.querySelector("#numberOfRequests");
    numberOfRequests.innerText = requests;
}

function logOut(element) {
    if (element.innerText == "Sign Out"){
        element.innerText = "Sign In";
    }
    else {
        element.innerText = "Sign Out";
    }
}

function like(element){
    alert('Ninja was liked');
}

function changeName(element){
    var x = document.getElementById("new_name").value;
    document.getElementById("name").innerHTML = x;
}