var dic map[[2]int]int

func dp(text1 string, text2 string, x int, y int) int {
    key := [2]int{x,y}
    if _, ok := dic[key]; !ok {
        if x == 0 || y == 0 {
            dic[key] = 0
        } else if text1[x-1] == text2[y-1] {
            dic[key] = dp(text1, text2, x-1, y-1) + 1
        } else {
            dic[key] = max(
                dp(text1, text2, x, y-1),
                dp(text1, text2, x-1, y),
            )
        }
    }
    return dic[key]
}

func longestCommonSubsequence(text1 string, text2 string) int {
    dic = make(map[[2]int]int)
    return dp(text1, text2, len(text1), len(text2))
}