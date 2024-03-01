import "strings"

func maximumOddBinaryNumber(s string) string {
    dic := make(map[int]int)
    for _, i := range s {
        val := int(i - '0')
        dic[val] += 1 
    }
    return strings.Repeat("1", dic[1]-1) + strings.Repeat("0", dic[0]) + "1"
}