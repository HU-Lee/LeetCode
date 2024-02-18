type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {

    const dic = new Map()
    
    return function(...args: number[]) {
        const key = args.join("_")
        if (dic.has(key)) {
            return dic.get(key)
        } else {
            dic.set(key, fn(...args))
            return dic.get(key)
        }   
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */