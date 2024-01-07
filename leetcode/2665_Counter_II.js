/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

var createCounter = function(init) {
    let curr_init = init;
    function increment() {
        return ++curr_init;
        }
    function decrement() {
        return --curr_init;
    }
    function reset() {
        curr_init = init;
        return curr_init;
    }
    return {increment, decrement, reset}
};


/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */