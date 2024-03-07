declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    return this.reduce(
        (init, val) => {
            const key = fn(val);
            if (key in init) {
                init[key].push(val)
            } else {
                init[key] = [val]
            }
            return init
        }
    , {})
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */