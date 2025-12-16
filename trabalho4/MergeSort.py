class MergeSort:
    def sort(self, arr):
        stats = {'comps': 0, 'swaps': 0}
        
        def _merge_sort(curr_arr):
            if len(curr_arr) > 1:
                mid = len(curr_arr) // 2
                L = curr_arr[:mid]
                R = curr_arr[mid:]

                _merge_sort(L)
                _merge_sort(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    # Count comparison
                    stats['comps'] += 1
                    
                    if L[i] < R[j]:
                        curr_arr[k] = L[i]
                        stats['swaps'] += 1 
                        i += 1
                    else:
                        curr_arr[k] = R[j]
                        stats['swaps'] += 1 
                        j += 1
                    k += 1

                while i < len(L):
                    curr_arr[k] = L[i]
                    stats['swaps'] += 1
                    i += 1
                    k += 1

                while j < len(R):
                    curr_arr[k] = R[j]
                    stats['swaps'] += 1
                    j += 1
                    k += 1
        _merge_sort(arr)
        return arr, stats['comps'], stats['swaps']