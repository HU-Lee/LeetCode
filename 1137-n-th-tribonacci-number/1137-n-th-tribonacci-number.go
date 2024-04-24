var dic = map[int]int{
    0:0,
    1:1,
    2:1,
}

func tribonacci(n int) int {
    if _, ok := dic[n]; !ok {
        dic[n] = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
    }
    return dic[n]
}