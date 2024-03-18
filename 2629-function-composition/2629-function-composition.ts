type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        let y = x;
        functions.reverse().forEach((f) => {
            y = f(y)
        })
        return y
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */