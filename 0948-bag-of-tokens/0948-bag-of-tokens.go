import "sort"

func bagOfTokensScore(tokens []int, power int) int {
    sort.Ints(tokens)
    score := 0
    max := 0
    status := power
    for len(tokens) > 0 {
        if status >= tokens[0]{
            status -= tokens[0]
            tokens = tokens[1:]
            score += 1
            if max < score {
                max = score
            }
        } else if score > 0 {
            status += tokens[len(tokens)-1]
            tokens = tokens[:len(tokens)-1]
            score -= 1
        } else {
            break
        }
    }
    return max
}