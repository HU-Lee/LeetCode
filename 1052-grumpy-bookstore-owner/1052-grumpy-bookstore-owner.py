class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        passive = sum(customers[i]*(1-grumpy[i]) for i in range(n))

        add = sum(customers[i]*grumpy[i] for i in range(minutes))
        mx = add
        for x in range(1, n):
            if x + minutes - 1 >= n:
                break
            left = x - 1
            right = x + minutes - 1
            add += customers[right]*grumpy[right] - customers[left]*grumpy[left]
            if add > mx:
                mx = add
        
        return passive + mx