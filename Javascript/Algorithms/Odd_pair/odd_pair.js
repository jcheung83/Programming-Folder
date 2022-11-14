function odd_pair(numbers){
    var dict = {};
    for (var i=0; i<numbers.length; i++){
        dict[numbers[i]] = (dict[numbers[i]] || 0) + 1;
    }
    for (key in dict){
        if (dict[key] % 2 == 1)
            return key;
    }
    return undefined;
}

const nums1 = [2, 2];
const expected1 = undefined;

const nums2 = [5, 3, 5, 3, 6, 6, 8];
const expected2 = 8;

const nums3 = [5, 4, 3, 4, 3, 4, 5, 4, 4];
const expected3 = 4; // there are two pairs of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 1, 10, 6, 3, 2, 5, 2];
const expected4 = 10;

console.log(odd_pair(nums1));
console.log(odd_pair(nums2));
console.log(odd_pair(nums3));
console.log(odd_pair(nums4));