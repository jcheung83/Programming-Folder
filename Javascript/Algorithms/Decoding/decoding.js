// decoding function, does not take into account edge cases 
// where users input multiple letters in a row
// such as "aabb"
function decoding(word){
    const temp = word;
    var new_word=[];
    var temp_holder;
    var count;
    if (temp === undefined){
        return word;
    }
    var i=0;
    while(i<temp.length){
        temp_holder=temp[i];
        var k=i+1;
        while(Number.isNaN(temp[k]*1)){
            k++;   
        }
        count=temp[k];
        
        for (var j=k+1; Number.isInteger(temp[j]*1); j++){
            count+=temp[j];
        }
        i=j;
        for (var x=0; x<count; x++){
            if (temp_holder != " "){
                new_word += temp_holder;
            }
        }
    }
    return new_word;
}

console.log(decoding("a0b5c8d20"));
console.log(decoding(" 3c12 4 5a10"));
console.log(decoding("c1d1e1f1g1h1i1j1"))
console.log(decoding("aaa3bb5c5ddd6e4f"))


