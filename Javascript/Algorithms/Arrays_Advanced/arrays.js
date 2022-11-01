var arr2d2 = [ [2, 5, 8],[3, 6, 1],[5, 7, 7],[6, 1, 3, 5, 6, 7, 8, 9, 10, 11] ];

function flatten(temp) {
    var flat = [];
    for (var i=0; i<temp.length; i++){
        for (var j=0; j<temp[i].length; j++){
            flat.push(arr2d2[i][j]);
        }
    }
    return flat;
}

function isPresent2d(temp, value) {
    for (var i=0; i<temp.length; i++){
        for (var j=0; j<temp[i].length; j++){
            if (temp[i][j] == value)
                return true;
        }
    }
    return false;
}

var newArray = flatten(arr2d2);
console.log(newArray);
console.log(isPresent2d(arr2d2, 9));