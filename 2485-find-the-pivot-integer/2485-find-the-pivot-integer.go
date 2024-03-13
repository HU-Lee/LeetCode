func pivotInteger(n int) int {
    sum := 0
    for sum*sum < n*(n+1)/2 {
        sum++
    }
    if sum*sum == n*(n+1)/2 {
        return sum
    } else {
        return -1
    }
}