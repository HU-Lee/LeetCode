class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a == b
        # 0 = a^a == a^b
        # (XOR from i to k) == 0
        # (XOR from 0 to k) == (XOR from 0 to i-1) (i>0)
        # (XOR from 0 to k) == 0                   (i=0)

        cnt = 0

        l = len(arr)
        xors = [0]*l
        xors[0] = arr[0]
        for i in range(l):
            xors[i] = xors[i-1] ^ arr[i]
            if xors[i] == 0:
                cnt += i

        for i in range(1, l):
            for k in range(i+1, l):
                if xors[i-1] == xors[k]:
                    print(k,i-1)
                    cnt += k-i

        return cnt