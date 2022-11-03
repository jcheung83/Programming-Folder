function rotate_string(word, number){
    if (number > word.length)
        number %= word.length;
    if (number == 0)
        return word;
    var new_string="";
    number = word.length-number;
    for (var i=0; i<word.length; i++){
        new_string += word[number];
        number++;
        if (number == word.length)
            number = 0;
        console.log(new_string);
    }
    return new_string;
}

// function rotate_string(str, num) {
//     if (num > str.length)
//         num %= str.length;
//     if (num == 0)
//         return str;
//     str = str.substring(str.length-num) + str.substring(0, str.length-num);
//     return str;
// }

// function rotateString(str, num) {
//     var rotations = num%str.length;
//     return str.substring(str.length-rotations) + str.substring(0, str.length-rotations);
// }

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor"; 

console.log(rotate_string(str, 0));
console.log(rotate_string(str, 1));
console.log(rotate_string(str, 2));
console.log(rotate_string(str, 4));
console.log(rotate_string(str, 13));