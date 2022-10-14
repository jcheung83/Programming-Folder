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
    var name = document.querySelector("#name");
    var random = Math.floor(Math.random() * 11);
    console.log(random);
    if (random==0){
        name.innerText = "Bobby Dee";
    }
    else if (random==1){
        name.innerText = "Lame Duck";
    }
    else if (random==2){
        name.innerText = "Poppy Seed";
    }
    else if (random==3){
        name.innerText = "Random Name";
    }
    else if (random==4){
        name.innerText = "People Person";
    }
    else if (random==5){
        name.innerText = "Henry Winkler";
    }
    else if (random==6){
        name.innerText = "Joe Biden";
    }
    else if (random==7){
        name.innerText = "Stan the Man";
    }
    else if (random==8){
        name.innerText = "Smash Mouth";
    }
    else if (random==9){
        name.innerText = "Clayton Crain";
    }
    else if (random==10){
        name.innerText = "John Doer";
    }
    else {
        name.innerText = "Fail";
    }
}