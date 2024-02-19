class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = [2**i for i in range(0,32)]
        return n in arr
        