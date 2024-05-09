class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        selected = happiness[:k]
        return sum(max(0, x-idx) for idx, x in enumerate(selected))