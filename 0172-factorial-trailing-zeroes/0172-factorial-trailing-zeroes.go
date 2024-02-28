func trailingZeroes(n int) int {
    sum := 0
    for n > 0 {
        n = n/5
        sum += n
    }
    return sum
}