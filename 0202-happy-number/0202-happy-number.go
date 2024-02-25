func isHappy(n int) bool {
    var arr []int
    s := n
    for !contains(arr, s) {
        arr = append(arr, s)
        s = process(s)
    }
    return s == 1
}

func process(i int) int {
    sum := 0
    for i > 0 {
        r := i%10
        sum += r*r
        i = i / 10
    }
    return sum
}

func contains(s []int, e int) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}