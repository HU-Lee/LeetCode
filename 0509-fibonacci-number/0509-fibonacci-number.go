var dic =  map[int]int{
    0:0,
    1:1,
}

func fib(n int) int {
    if val, ok := dic[n]; !ok {
        dic[n] = fib(n-1) + fib(n-2)
        return dic[n]
    } else {
        return val
    }
}