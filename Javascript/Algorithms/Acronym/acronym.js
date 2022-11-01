function acronym(words) {
    if (words == undefined){
        return;
    }
    const myArray = words.split(" ");
    var acronym = ""
    for (var i = 0; i<myArray.length; i++){
        if (myArray[i][0] != undefined){
            acronym += myArray[i][0].toUpperCase();
        }
    }
    return acronym;
}

function acronym2(words) {
    if (words == undefined){
        console.log("undefined")
        return;
    }
    const myArray = words;
    var acronym = "";
    for (var i = 0; i<myArray.length; i++){
        if(i == 0 && myArray[i] != " "){
            acronym += myArray[i].toUpperCase();
        }
        if ((myArray[i-1] == " ") && (myArray[i] != " ") && (myArray[i] != undefined)){
            acronym += myArray[i].toUpperCase();
        }
    }
    return acronym;
}

console.log(acronym2("object oriented programming"));
console.log(acronym2("federal bureau investigation"));
console.log(acronym2("bunch of stuff that I am writing to see what it gives me"));
console.log(acronym2("       "))
console.log(acronym2("  a b c  d e f g   hi i     j"))
