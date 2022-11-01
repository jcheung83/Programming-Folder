function create_dictionary(arr1){
    let dict1={};
    for (var i=0; i<arr1.length; i++){
        dict1[arr1[i]] = (dict1[arr1[i]] || 0) + 1;
    }
    return dict1;
}

const arr1 = ["a", "a", "a"];
const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const arr3 = ["ab", "bb", "BB", "bB", "AB", "ab", "bb", "Bb"];
const arr4 = [];
const arr5 = [" "];
console.log(create_dictionary(arr1));
console.log(create_dictionary(arr2));
console.log(create_dictionary(arr3));
console.log(create_dictionary(arr4));
console.log(create_dictionary(arr5));









