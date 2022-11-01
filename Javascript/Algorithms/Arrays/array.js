//always hungry
function alwaysHungry(arr){
    var food=0;
    for (var i=0; i<arr.length; i++){
        if (arr[i]=="food"){
            console.log("yummy");
            food++;
        }
    }
    if (food==0){
        console.log("I'm hungry");
    }
}

//high pass filter
function highPass(arr, cutoff) {
    var filteredArr = [];
    for (var i=0; i<arr.length; i++){
        if (arr[i] > cutoff){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

//better than average
function betterThanAverage(arr) {
    var sum = 0;
    // calculate the average
    for (var i=0; i<arr.length; i++){
        sum += arr[i];
    }
    var average = sum / arr.length;
    var count = 0
    // count how many values are greated than the average
    for (var i=0; i<arr.length; i++){
        if (arr[i]>average){
            count++;
        }
    }
    return count;
}

//array reverse
function reverse(arr) {
    var revArr=[];
    for (var i=arr.length-1; i>=0; i--){
        revArr.push(arr[i]);
    }
    return revArr;
}

//fibonacci array
function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for (var i=2; i<n; i++){
        fibArr.push(fibArr[i-1]+fibArr[i-2]);
    }
    return fibArr;
}

//always hungry
alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"

//high pass filter
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]

//better than average
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4

//array reverse
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]

//fibonacci array
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]