class CountingSort:
    def sort(self, arr):
        if not arr:
            return arr, 0, 0
        
        max_val = max(arr)
        min_val = min(arr)
        range_of_elements = max_val - min_val + 1
        comps = 0
        swaps = 0
        
        count = [0] * range_of_elements
        output = [0] * len(arr)
        
        for num in arr:
            count[num - min_val] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        for num in reversed(arr):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
            swaps += 1  
        
        return output, comps, swaps