class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur = customers[0][0]
        total_wait = 0

        for a, t in customers:
            if a <= cur:
                total_wait += cur + t - a
                cur += t
            else:
                total_wait += t
                cur = a + t
        
        return total_wait / len(customers)