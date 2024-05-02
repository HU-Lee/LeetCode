function findMaxK(nums: number[]): number {
    let ans = -1
    const dic = {}

    for (const num of nums) {
        dic[-num] = true
        if (dic[num] && Math.abs(num) > ans) {
            ans = Math.abs(num)
        }
    }
    return ans
};