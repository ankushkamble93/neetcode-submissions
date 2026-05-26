class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            prev_index = merged[-1]
            if current[0] <= prev_index[1]:
                prev_index[1] = max(current[1], prev_index[1])
            else:
                merged.append(current)
        return merged