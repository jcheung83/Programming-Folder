var count = [9,12,985];

function whenLiked1(i){
    count[i]++;
    console.log(count[i]);
    var numberOfLikes = document.querySelector("#numberOfLikes1")
    numberOfLikes.innerText = count[i] + " like(s)";
}

function whenLiked2(i){
    count[i]++;
    console.log(count[i]);
    var numberOfLikes = document.querySelector("#numberOfLikes2")
    numberOfLikes.innerText = count[i] + " like(s)";
}

function whenLiked3(i){
    count[i]++;
    console.log(count[i]);
    var numberOfLikes = document.querySelector("#numberOfLikes3")
    numberOfLikes.innerText = count[i] + " like(s)";
}