function change(amount){
    var dictionary = {};
    if (amount >= 25){
        dictionary['quarter'] = Math.floor(amount/25);
        amount %= 25;
    }
    if (amount >= 10){
        dictionary['dime'] = Math.floor(amount/10);
        amount %= 10;
    }
    if (amount >= 5){
        dictionary['nickel'] = Math.floor(amount/5);
        amount %= 5;
    }
    if (amount >= 1){
        dictionary['penny'] = amount;
    }
    return dictionary;
}

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 }; 

const cents5 = 94;
const expected5 = { quarter: 3, dime: 1, nickel: 1, penny: 4 }; 

const cents6 = 234234324;

console.log(change(cents1));
console.log(change(cents2));
console.log(change(cents3));
console.log(change(cents4));
console.log(change(cents6));

