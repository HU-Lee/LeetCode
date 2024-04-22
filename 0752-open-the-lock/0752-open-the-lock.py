class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def changeLock(lock: str, idx: int, reverse: bool) -> str:
            numbers = "0123456789"    
            v = int(lock[i])    
            lock_arr = list(lock)
            if reverse:
                lock_arr[i] = numbers[v-1]
            else:
                lock_arr[i] = numbers[(v+1)%10]
            return "".join(lock_arr)

        q = [("0000",0)]
        visited = defaultdict(bool)
        visited["0000"] = True

        while q:
            lock, x = q.pop(0)
            if lock == target:
                return x
            elif lock in deadends:
                continue
            for i in range(4):
                l1 = changeLock(lock, i, True)
                if (not visited[l1]) and (not l1 in deadends):
                    visited[l1] = True
                    q.append((l1, x+1))
                l2 = changeLock(lock, i, False)
                if (not visited[l2]) and (not l2 in deadends):
                    visited[l2] = True
                    q.append((l2, x+1))
        return -1