def find_monotonicity_changes(arr):
    changes = []
    
    if len(arr) < 2:
        return changes
    
    is_increasing = None
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                changes.append(i)
                is_increasing = True
        elif arr[i] < arr[i - 1]:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                changes.append(i)
                is_increasing = False
    
    return changes

# Test cases
print(find_monotonicity_changes([0, 1]))          # Output: []
print(find_monotonicity_changes([0, 2, 1]))      # Output: [1]
print(find_monotonicity_changes([0, 1, 1, 0]))  # Output: [2]
