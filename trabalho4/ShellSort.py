class ShellSort:
    def sort(self, arr):
        n = len(arr)
        gap = n // 2
        comps = 0
        swaps = 0
        
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                
                while j >= gap:
                    comps += 1  
                    if arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        swaps += 1
                        j -= gap
                    else:
                        break  
                
                arr[j] = temp
            gap //= 2
        return arr, comps, swaps