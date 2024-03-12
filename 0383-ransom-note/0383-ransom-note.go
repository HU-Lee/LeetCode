func canConstruct(ransomNote string, magazine string) bool {
    dic := make(map[rune]int)

    for _, s := range magazine {
        if _, ok := dic[s]; !ok {
            dic[s] = 1
        } else {
            dic[s] += 1
        }
    }
    for _, s := range ransomNote {
        if val, ok := dic[s]; !ok {
            return false
        } else if val <= 0 {
            return false
        } else {
            dic[s] -= 1
        }
    }
    return true
}