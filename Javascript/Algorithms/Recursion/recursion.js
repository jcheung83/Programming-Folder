function sum(n){
    if (n<1)
        return 0;
    n = parseInt(n);
    return (n + sum(n-1));
}

function sum2(n){
    if (n[0] == undefined)  
        return 0;
    return (n.shift() + sum2(n));
}

const num1 = [1, 2, 3.8, 4.5, 5, 6, 7, 8, 9.1, 10];
console.log(sum2(num1));