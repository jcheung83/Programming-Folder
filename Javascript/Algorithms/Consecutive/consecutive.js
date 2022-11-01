function consecutive(word) {
    var new_word = "";
    var temp_holder = "";
    const temp = word;
    if (word == undefined){
        return;
    }
    else {
        temp_holder = temp[0];
        new_word += temp[0];
        var count = 1;
        for (var i=1; i<temp.length; i++){
            if (temp[i] == temp_holder){
                count++
            }
            else {
                new_word += count;
                new_word += temp[i];
                temp_holder = temp[i];
                count=1;
            }
        }
        new_word += count;
    }
    if (new_word.length >= word.length){
        return word;
    }
    return new_word;
}

console.log(consecutive("wooords"));
console.log(consecutive("a"));
console.log(consecutive("aa"));
console.log(consecutive("aabb"));
console.log(consecutive("aaaaaaac"));
console.log(consecutive(" "));
console.log(consecutive("beeeeeeeeeeeeeeeeeeeetlejuice"))
console.log(consecutive("  a  3  f  aaaaa  3  4"));