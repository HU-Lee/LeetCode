func timeRequiredToBuy(tickets []int, k int) int {
    sum := 0
    x := tickets[k]
    for idx, t := range tickets {
        if idx <= k {
            sum += min(t,x)
        } else {
            sum += min(t,x-1)
        }
    }
    return sum
}