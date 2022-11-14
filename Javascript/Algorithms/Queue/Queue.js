function six_feet(queue){
    var count = [];
    for (var i=0; i<queue.length; i++){
        if (queue[i] == 1){
            count.push(i);
            if (count.length > 1 && (count[count.length-1]-count[count.length-2] < 7 ))
                return false;
        }
    }
    return true;
}

const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

console.log(six_feet(queue1));
console.log(six_feet(queue2));
console.log(six_feet(queue3));
console.log(six_feet(queue4));