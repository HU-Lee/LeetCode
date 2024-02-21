import "math"

func rangeBitwiseAnd(left int, right int) int {
    sum := 0
	for i := 0; i < 32; i++ {
		exp := int(math.Pow(2,float64(i)))
		if right-left+1 > exp {
			continue
		} else {
			bit := left & right
			if (bit / exp) % 2 == 1 {
				sum += exp
			} 
		}
	}
    return sum
}