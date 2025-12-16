class HeapSort:
    def heapify(self, arr, n, i, stats):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            stats['comps'] += 1  
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            stats['comps'] += 1  
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            stats['swaps'] += 1  
            
            self.heapify(arr, n, largest, stats)

    def sort(self, arr):
        n = len(arr)
        stats = {'comps': 0, 'swaps': 0}

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i, stats)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            stats['swaps'] += 1
            
            self.heapify(arr, i, 0, stats)

        return arr, stats['comps'], stats['swaps']