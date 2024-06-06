class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        if l % groupSize != 0:
            return False
        dic = collections.defaultdict(int)
        for h in hand:
            dic[h] += 1

        cards = sorted(dic.keys())
        
        for c in cards:
            if dic[c] > 0:
                tmp = dic[c]
                for i in range(c, c + groupSize):
                    if dic[i] < tmp:
                        return False
                    dic[i] -= tmp
        return True