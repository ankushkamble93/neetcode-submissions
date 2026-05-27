class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        first_interval = [intervals[0]]
        for current in intervals[1:]:
            prev_index = first_interval[-1]
            if current[0] <= prev_index[1]:
                prev_index[1] = max(prev_index[1], current[1])
            else:
                first_interval.append(current)
        return first_interval
            

