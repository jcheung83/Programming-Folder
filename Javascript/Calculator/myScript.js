var num=[];
var numberCount=0;
var calculation;
var operation=[];
var newNum=0;

function setOP(operator){
    var displayDiv = document.querySelector("#display");
    var displayNumber = displayDiv.innerHTML;
    num.push(displayNumber);
    numberCount++;
    newNum = 1;
    operation.push(operator);
}

function press(number){
    var displayDiv = document.querySelector("#display");
    var displayNumber = displayDiv.innerHTML;
    if (displayNumber != 0 && newNum == 0){
        number = displayNumber + number;
    }
    displayDiv.innerHTML = number;
    newNum = 0;
}

function calculate(){
    var displayDiv = document.querySelector("#display");
    var displayNumber = displayDiv.innerHTML;
    num.push(displayNumber);
    newNum = 0;
    numberCount++;
    if (operation[0] == '+'){
        calculation = (num[0]*1) + (num[1]*1);
    }
    else if (operation == '-'){
        calculation = (num[0]*1) - (num[1]*1);
    }
    else if (operation == '*'){
        calculation = (num[0]*1) * (num[1]*1);
    }
    else if (operation == '/'){
        calculation = (num[0]*1) / (num[1]*1);
    }
    
    if (num.length > 2){
        for (var i=2; i<numberCount; i++){
            if (operation[i-1] == '+'){
                calculation += (num[i]*1);
            }
            else if (operation[i-1] == '-'){
                calculation += (num[i]*1);
            }
            else if (operation[i-1] == '*'){
                calculation *= (num[i]*1);
            }
            else if (operation[i-1] == '/'){
                calculation /= (num[i]*1);
            }
        }
    }
    displayDiv.innerHTML = calculation;
}

function clr(){
    var displayDiv = document.querySelector("#display");
    num = [];
    numberCount = 0;
    calculation = 0;
    operation = [];
    displayDiv.innerText = "0";
}
