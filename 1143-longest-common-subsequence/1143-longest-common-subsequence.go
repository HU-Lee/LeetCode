
func longestCommonSubsequence(text1 string, text2 string) int {
    arr := make([][]int, len(text1)+1)
    for i := range arr {
        arr[i] = make([]int, len(text2)+1)
    }
    for y := 0; y <= len(text2); y++ {
        for x := 0; x <= len(text1); x++ {
            if x == 0 || y == 0 {
                arr[x][y] = 0
            } else if text1[x-1] == text2[y-1] {
                arr[x][y] = arr[x-1][y-1] + 1
            } else {
                arr[x][y] = max(arr[x-1][y], arr[x][y-1])
            }
        }
    }
    return arr[len(text1)][len(text2)]
}