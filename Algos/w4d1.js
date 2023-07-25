/* 
Recursively sum an arr of ints
*/

const two_nums1 = [1, 2, 3];
const two_expected1 = 6;

const two_nums2 = [1];
const two_expected2 = 1;

const two_nums3 = [];
const two_expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */

// normal function -> with a for/while loop
function sumArr(nums) {}


// recursive function
function recursiveSumArr(nums) {
    //edge case
    if (nums.length === 0){
        return 0
    }
    return nums.pop() + recursiveSumArr(nums)

}
console.log(recursiveSumArr(two_nums1));


/*****************************************************************************/

/* 
Recursive Sigma

Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) {
    num = Math.floor(num)
    if (num < 1){     
        return 0;
    }
    else{
        return num +  recursiveSigma(num-1)
    }
}

console.log(recursiveSigma(num3));