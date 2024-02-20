func sumWealth(numbers []int) int {
    sum := 0
    for _, num := range numbers {
        sum += num
    }
    return sum
}

func maximumWealth(accounts [][]int) int {
    max := 0
    for _, account := range accounts {
        wealth := sumWealth(account)
        if max < wealth {
            max = wealth
        }
    }
    return max
}