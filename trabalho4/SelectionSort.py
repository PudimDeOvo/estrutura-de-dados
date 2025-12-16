class SelectionSort:
    def sort(self, arr):
        comps = 0
        swaps = 0
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                comps += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                swaps += 1
        return arr, comps, swaps