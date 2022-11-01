function find_solo(arr2){
    var count=0;
    for (var i=0; i<arr2.length; i++){
        for (var j=0; j<arr2.length; j++){
            if (arr2[i] == arr2[j]){
                count++;
            }
        }
        if (count%2 === 1){
            return arr2[i];
        }
        else {
            count = 0;
        }
    }
}

const nums0 = [5, 4, 3, 2, 1, 9, 9, 1, 2, 3, 4, 5, 6]
const nums1 = [1];
const nums2 = [5, 4, 5];
const nums3 = [5, 4, 3, 4, 3, 4, 5];
const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];

console.log(find_solo(nums0));
console.log(find_solo(nums1));
console.log(find_solo(nums2));
console.log(find_solo(nums3));
console.log(find_solo(nums4));