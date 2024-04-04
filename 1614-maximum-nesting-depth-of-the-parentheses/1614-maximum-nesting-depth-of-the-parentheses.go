func maxDepth(s string) int {
    ans := 0
    c := 0
    for _, i := range s {
        if i == '(' {
            c++
            if c > ans {
                ans = c
            }
        } else if i == ')' {
            c--
        }
    }
    return ans
}