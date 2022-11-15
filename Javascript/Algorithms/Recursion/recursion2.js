function rFact(n){
    if (n < 1)
        return 1;
    return (parseInt(n) * parseInt(rFact(n-1)));
}

const num1 = 3;
const expected1 = 6;
// Explanation: 123 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 123456 = 720

const num3 = 0;
const expected3 = 1;

console.log(rFact(num1));
console.log(rFact(num2));
console.log(rFact(num3));

function fibonacci(n){
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    return (fibonacci(n-1) + fibonacci(n-2))
}

for (var x=0; x<20; x++){
    console.log(x,":",fibonacci(x));
}