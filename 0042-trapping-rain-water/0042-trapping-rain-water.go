func trap(height []int) int {
    n := len(height)
    ans := 0
    tmp,base := 0,-1
    for i := 0; i<n; i++ {
        h := height[i]
        if h >= base {
            ans += tmp
            tmp = 0
            base = h
        } else {
            tmp += (base-h) 
        }
    }
    mx := base
    tmp,base = 0,-1
    for i := n-1; i>=0; i-- {
        if base == mx {
            break
        }
        h := height[i]
        if h >= base {
            ans += tmp
            tmp = 0
            base = h
        } else {
            tmp += (base-h) 
        }
    }
    return ans
}