func leastInterval(tasks []byte, n int) int {
    dic := make(map[byte]int)
    l := len(tasks)
    m := 0
    for _, task := range tasks {
        if val, ok := dic[task]; !ok {
            dic[task] = 1
        } else {
            dic[task] = val + 1
            if val + 1 > m {
                m = val + 1
            }
        }
    } 
    x := 0
    for _, val := range dic {
        if val == m {
            x++
        }
    }
    fmt.Println(m,n,x)
    cnt := (m-1)*(n+1) + x
    if cnt > l {
        return cnt
    } else {
        return l
    }
}