/* 
  Recursively reverse a string
  helpful methods:

  str.slice(beginIndex[, endIndex])
  returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

const str3 = "it works"

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStr(str) {
    //starting point
    //test case
    if (str.length <=1){
        return str
    }
    return str[str.length-1] + reverseStr(str.substring(0, str.length-1))
}

console.log(reverseStr(str1));
console.log(reverseStr(str2));
console.log(reverseStr(str3));

/*****************************************************************************/

/* 
  Return the fibonacci number at the nth position, recursively.
  
  Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

  The next number is found by adding up the two numbers before it,
  starting with 0 and 1 as the first two numbers of the sequence.
*/

const two_num1 = 0;
const two_expected1 = 0;

const two_num2 = 1;
const two_expected2 = 1;

const two_num3 = 2;
const two_expected3 = 1;

const two_num4 = 3;
const two_expected4 = 2;

const two_num5 = 4;
const two_expected5 = 3;

const two_num6 = 8;
const two_expected6 = 21;

/**
 * Recursively finds the nth number in the fibonacci sequence.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num The position of the desired number in the fibonacci sequence.
 * @returns {number} The fibonacci number at the given position.
 */
// with memoization
function fibonacci(num , memo = {0:0, 1:1}) {
    if (num <=1) return num;

    if (memo[num] !== undefined) return memo[num]

    memo[num] = fibonacci(num-1, memo) + fibonacci(num-2, memo)

    return memo[num]

    // return fibonacci(num-1) + fibonacci(num-2)


}
console.log(fibonacci(50));