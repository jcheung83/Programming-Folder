function dedupe (word) {
    var word1 = [];
    for (var x=0; x<word.length; x++){
        word1.push(word[x]);
    }
    for (var i=word1.length-1; i>=0; i--){
        console.log("i =", i, "word1[i] =", word1[i]);
        for (var j=i-1; j>=0; j--){
            console.log("j =", j, "word1[j] =", word1[j]);
            if (word1[j] === word1[i]){
                word1.splice(j,1);
            }
            console.log("array length =",word1.length)
        }
    }
    word = word1.join('');
    return word;
}

// function dedupe(str) {
//     var result = "";
//     for (var i=str.length-1; i>=0; i--)
//         if (result.indexOf(str[i]) == -1)
//             result = str[i] + result;
//     return result;
// }

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "hhelloooohoooh";
const expected2 = "eloh";

const str3 = "gabgcgdegfgg";
const expected3 = "abcdefg 1";

const str4 = "aaAAaa";
const expected4 = "Aa"; 

const str5 = "abcdefghaceg";
const expected5 = "bdfhaceg";

const str6 = "       zz";
const expected6 = " z";

// console.log(dedupe(str1));
// console.log(dedupe(str2));
console.log(dedupe(str3));
// console.log(dedupe(str4));
// console.log(dedupe(str5));
// console.log(dedupe(str6));