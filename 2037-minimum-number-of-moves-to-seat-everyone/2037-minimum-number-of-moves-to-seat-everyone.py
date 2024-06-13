class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        return sum(abs(seats[i]-students[i]) for i in range(len(seats)))