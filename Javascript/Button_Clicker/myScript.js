var likes1 = 13;
var likes2 = 37;

function hide(element) {
    element.remove();
}

function logIn(element) {
    element.innerText = "Logout";
}

function whenLiked1(element) {
    alert('Ninja was liked');
    likes1++;
    var temp = document.querySelector("#likes1");
    console.log(temp);
    temp.innerHTML = likes1 + " likes";
}

function whenLiked2(element) {
    alert('Ninja was liked');
    likes2++;
    var temp = document.querySelector("#likes2");
    console.log(temp);
    temp.innerHTML = likes2 + " likes";
}