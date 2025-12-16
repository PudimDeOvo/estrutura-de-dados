class QuickSort:
    def sort(self, arr):
        stats = {'comps': 0, 'swaps': 0}

        def partition(low, high):
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                stats['comps'] += 1
                
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    stats['swaps'] += 1
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            stats['swaps'] += 1
            return i + 1

        def _quick_sort(low, high):
            if low < high:
                pi = partition(low, high)
                _quick_sort(low, pi - 1)
                _quick_sort(pi + 1, high)

        _quick_sort(0, len(arr) - 1)
        return arr, stats['comps'], stats['swaps']