function inventory(newInv, currInv){
    for (var i=0; i<newInv.length; i++){
        var isInDictionary = 0;
        for (var j=0; j<currInv.length; j++){
            console.log(newInv[i].name, currInv[j].name);
            if (currInv[j].name === newInv[i].name){
                currInv[j].quantity += newInv[i].quantity;
                isInDictionary = 1;
                break;
            }           
        }
        if (!isInDictionary)
            currInv.push(
                { name: newInv[i].name, quantity: newInv[i].quantity }
            );
    }
    return currInv;
}

const newInv1 = [
    { name: "Grain of Rice", quantity: 9000 },
    { name: "Peanut Butter", quantity: 520 },
    { name: "Royal Jelly", quantity: 201 },
    { name: "Pillows", quantity: 1 }
];
const currInv1 = [
    { name: "Peanut Butter", quantity: 200 },
    { name: "Grain of Rice", quantity: 111 },
    { name: "Royal Jelly", quantity: 2 }
];
const expected1 = [
    { name: "Peanut Butter", quantity: 720 },
    { name: "Grain of Rice", quantity: 9111 },
    { name: "Royal Jelly", quantity: 203 },
    { name: "Pillows", quantity: 1 }
];

console.log(inventory(newInv1, currInv1));