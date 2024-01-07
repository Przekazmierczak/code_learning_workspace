/**
 * @return {Function}
 */
var createHelloWorld = function() {
    function hello() {
        return "Hello World"
    }
    return hello
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */