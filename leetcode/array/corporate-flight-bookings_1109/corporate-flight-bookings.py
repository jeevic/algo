
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0 for i in range(n)]
        for s, e, v in bookings:
            i = s -1
            while i < e:
                answer[i] += v
                i += 1
        return answer




class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for i in range(n)]
        for s, e, v in bookings:
           diff[s-1] += v
           if e < n:
               diff[e] -= v
        answer = [0 for i in range(n)]
        answer[0] = diff[0]
        idx = 1
        while idx < n:
            answer[idx] = answer[idx -1] + diff[idx]
            idx += 1
        return answer


