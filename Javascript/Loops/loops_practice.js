//print odds 1-20
console.log("Print odd numbers between 1 and 20:");
for (var i=1; i<21; i++){
    if (i%2 == 1){
        console.log(i);
    }
}

//decreasing multiples of 3
console.log("Print decreasing multiples of 3 from 100 to 0:");
for (var i=100; i>=0; i--){
    if (i%3 == 0){
        console.log(i);
    }
}

//print the sequence
console.log("Print the sequence:")
var sequence = [4, 2.5, 1, -0.5, -2, -3.5];
for (var i=0; i<sequence.length; i++){
    console.log(sequence[i]);
}

//sigma
console.log("Add the values from 1 to 100:")
var sum=0;
for (var i=0; i<101; i++){
    sum += i;
}
console.log(sum);

//factorial
console.log("Multiply the values from 1-12:")
var product=1;
for (var i=1; i<=12; i++){
    product = product * i;
}
console.log(product);

//reversing an array
console.log("Reversing an arry:")
var myArray=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
var temp;
for (var i=0; i<myArray.length/2; i++){
    temp = myArray[i];
    myArray[i] = myArray[myArray.length-1-i];
    myArray[myArray.length-1-i] = temp;
}

console.log(myArray);