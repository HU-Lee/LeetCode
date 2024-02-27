

func isPalindrome(x int) bool {
    rev_x := 0;
    mul := 1;
    for mul <= x {
        mul *= 10
    }
    n := x
    for n > 0 {
        mul /= 10
        rev_x += mul*(n%10)
        n = n/10
    }
    return rev_x == x
}