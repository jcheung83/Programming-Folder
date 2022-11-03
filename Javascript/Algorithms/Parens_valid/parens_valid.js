function parens_valid (word){
    var dict = {};
    var x = 0;
    var count_open_p = 0;
    var count_open_s = 0;
    var count_open_c = 0;
    for (i in word){
        if (word[i] === '('){
            count_open_p++;
            dict[x] = word[i];
            x++;
        }
        else if (word[i] === '['){
            count_open_s++;
            dict[x] = word[i];
            x++;
        }
        else if (word[i] === '{'){
            count_open_c++;
            dict[x] = word[i];
            x++;
        }
        else if (word[i] === ')'){
            if (count_open_p === 0 || dict[x-1] != '(')
                return false;
            else {
                count_open_p--;
                x--;
            }
        }
        else if (word[i] === ']'){
            if (count_open_s === 0 || dict[x-1] != '[')
                return false;
            else {
                count_open_s--;
                x--;
            }
        }
        else if (word[i] === '}'){
            if (count_open_c === 0 || dict[x-1] != '{')
                return false;
            else {
                count_open_c--;
                x--;
            }
        }
    }
    return (count_open_p === 0 && count_open_s === 0 && count_open_c === 0);
}

// function parens_valid (word){
//     var dict = {};
//     var x = 0;
//     for (i in word){
//         if (word[i] === '('){
//             dict[x] = word[i];
//             x++;
//         }
//         else if (word[i] === '['){
//             dict[x] = word[i];
//             x++;
//         }
//         else if (word[i] === '{'){
//             dict[x] = word[i];
//             x++;
//         }
//         else if (word[i] === ')'){
//             if (dict[x-1] != '(')
//                 return false;
//             else {
//                 x--;
//             }
//         }
//         else if (word[i] === ']'){
//             if (dict[x-1] != '[')
//                 return false;
//             else {
//                 x--;
//             }
//         }
//         else if (word[i] === '}'){
//             if (dict[x-1] != '{')
//                 return false;
//             else {
//                 x--;
//             }
//         }
//     }
//     return true;
// }

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false; 


console.log(parens_valid(str1));
console.log(parens_valid(str2));
console.log(parens_valid(str3));