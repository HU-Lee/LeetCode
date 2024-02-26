func numberOfSteps(num int) int {
    ans := 0
    if num == 0 {
        return 0
    }
    for num > 1 {
        if num %2 == 0 {
            ans += 1 
        } else {
            ans += 2
        }
        num = num /2
    }
    return ans + 1
}