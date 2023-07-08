/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.

Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

const keys3 = ["abc", 3, "yo", "something"];
const vals3 = [42, "wassup", true];
const expected3 = {
    abc: 42,
    3: "wassup",
    yo: true,
    somehting: undefined
};

const keys4 = ["abc", 3, "yo"];
const vals4 = [42, "wassup", true, "something"];
const expected4 = false

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) { 
    //TODO if key.length != value.length => return false
    //TODO if length == 0, return false/null
    //! If value has no key
    if (keys.length < values.length){
        return false;
    }
    else if ( values.length == 0 || keys.length ==0){
        return {};
    }
    //else you continue
    let obj = {};

    //loop to populate the objects
    keys.forEach((keys,val) => {
        obj[keys] = values[val]
        //! If key has no value
        if(keys.length > values.length){
            obj[keys] = undefined;
        }

    });
    return obj;
}
console.log(zipArraysIntoMap(keys4,vals4));


/* 
  Invert Hash

  A hash table / hash map is an obj / dictionary

  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something:undefined };
const two_expected2 = false

const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey", test: "dicey", poop: "dicey" };
const two_expected3 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"] };

// no objects given will be empty, they will all at least have 1 key value pair

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */

// EXPLAIN COMPLEXITY (BIG O NOTATION)

function invertObj(obj) {
    // create a new object to return at the end
    let newObj = {}
    // iterate the given object
    for (const key in obj){
    // need to check if the value is undefined
        if(typeof obj[key] == 'undefined'){
      // if it is, we break the loop and just return false
            return false
    }
    // check if the key is already in newObj
        if(newObj.hasOwnProperty(obj[key])){
        // check if there is already an array attached to the key
            if(typeof newObj[obj[key]] == 'object'){
                newObj[obj[key]].push(key);
        } else {
            // create a array (because now we have 2 values with the same key)
            let newList = [];
            // make sure both values are in the array
            newList.push(newObj[obj[key]]);
            // add the current key we are on to the list
            newList.push(key);
            newObj[obj[key]] = newList;
        }
        } else {
            // for every key in the object, we need to do 2 things:
            // 1.create a new key using the current value (of the key we are on)
            // 2.set the value to the current key we are on
            newObj[obj[key]] = key
        }
    }
  // return the new object with the new switched key value pairs
    return newObj;
}

console.log(invertObj(two_obj3))