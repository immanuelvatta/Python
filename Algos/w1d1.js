/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 


    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
  */

const str1 = "aaaabbcdddaa";
const expected1 = "a4b2c1d3a2";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) { 
    //create an empty string to store the output
    let finalStr = "";
    let count = 1;
    //* create a for loop that loops through the string
    for (let i = 0; i < str.length; i++){
        if(str[i] == str[i+1]){
            count++;

        }else{
            finalStr += str[i] + count;
            count+1
        }
    }
    // if(finalStr.length < str.length){
    //     return finalStr;
    // }
    // else{
    //     return str;
    // }
    // condition          ?  (what do do if its true) : (what to do if its false)
    return finalStr.length < str.length ? finalStr : str
}

//   *****************************************************************************
    // loop through the string 0 point of the string to the end 
    // declare a counter variable and set it to one
    // loop through it again for 

/* 
    String Decode  
*/

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

console.log(encodeStr(str4))
/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) { }