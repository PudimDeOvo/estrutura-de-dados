class BubbleSort:
    def sort(self, arr):
        comps = 0
        swaps = 0
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                comps += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
        return arr, comps, swaps
    
    