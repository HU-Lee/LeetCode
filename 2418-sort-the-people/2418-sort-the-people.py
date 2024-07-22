class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[i], names[i]) for i in range(len(names))]
        return list(map(lambda x: x[1], sorted(people, reverse=True)))