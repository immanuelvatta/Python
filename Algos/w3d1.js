/* 
Balance Index

Here, a balance point is ON an index, not between indices.

Return the balance index where sums are equal on either side
(exclude its own value).

Return -1 if none exist.

*/

const two_nums1 = [-2, 5, 7, 0, 3];
const two_expected1 = 2;

const two_nums2 = [9, 9];
const two_expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {

    const len = nums.length
    // console.log(nums)
    if (len <= 2){
        return -1;
    }
    // create a left and right variable
    let left = nums[0]
    let right = 0

    // stack the right side (dont start at 0 or 1 index)
    for (let i = 2; i < len; i++){
        right += nums[i]
    }

    for (let i = 1; i < len-1; i++){
        // are the two sides the same?
        if(left == right){
            return i
        }
        right -= nums[i+1]
        left += nums[i]
    }
    return -1

}

console.log(balanceIndex(two_nums1));