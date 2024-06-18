class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        m = len(worker)

        jobs = sorted((difficulty[i], profit[i]) for i in range(n))
        print(jobs)

        worker.sort()

        j, w = 0,0
        tmp_profit = 0
        ans = 0
        while w < m:
            if j == n or jobs[j][0] > worker[w]:
                ans += tmp_profit
                w += 1
            else:
                tmp_profit = max(tmp_profit, jobs[j][1])
                j += 1

        return ans