/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res = [];
    for (i in arr) {
        if (fn(arr[i], i) === true) {
            res.push(arr[i]);
        }
    }
    return res;
};