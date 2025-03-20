# Interval Overlaping 
# Interval:[[1,3],[2,6],[8,10],[15,18]]
# Output : [[1,6],[8,10],[15,18]]

def merge(interval):
    ans = list()
    interval = sorted(interval)  # Sort intervals by start time

    for i in range(len(interval)):
        start = interval[i][0]
        end = interval[i][1]

        if ans and end <= ans[-1][1]:  # Use ans[-1] instead of ans[i]
            continue
        
        for j in range(i + 1, len(interval)):
            if interval[j][0] <= end:
                end = max(end, interval[j][1])
            else:
                break
        
        ans.append([start, end])  # Remove extra brackets

    return ans

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]
