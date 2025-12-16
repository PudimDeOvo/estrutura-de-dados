from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from ShellSort import ShellSort
from CountingSort import CountingSort
from HeapSort import HeapSort

def main():
    sorting_algorithms = {
        "Bubble Sort": BubbleSort(),
        "Insertion Sort": InsertionSort(),
        "Selection Sort": SelectionSort(),
        "Merge Sort": MergeSort(),
        "Quick Sort": QuickSort(),
        "Shell Sort": ShellSort(),
        "Counting Sort": CountingSort(),
        "Heap Sort": HeapSort()
    }
    
    test_list = [
        [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
        [100, 48, 19, 61, 86, 33, 13, 43, 84, 28],
        [81, 60, 6, 49, 40, 41, 38, 64, 44, 36],
        [45, 27, 11, 89, 63, 39, 9, 58, 52, 17],
        [88, 77, 26, 62, 30, 96, 56, 65, 98, 99],
        [76, 73, 16, 95, 35, 87, 68, 69, 51, 92],
        [37, 75, 90, 82, 8, 18, 23, 93, 57, 10],
        [15, 97, 14, 29, 7, 24, 31, 59, 78, 85],
        [5, 70, 55, 91, 47, 72, 2, 20, 34, 74],
        [50, 66, 32, 22, 54, 79, 21, 1, 80, 46]
    ]
    
    print(f"{'Algorithm':<15} | {'Test':<4} | {'Comparisons':<11} | {'Swaps':<8}")
    print("-" * 50)
    test_id = 0
    
    for name, algorithm_instance in sorting_algorithms.items():
        for i, original_case in enumerate(test_list):
            test_id = i + 1
            try:
                sorted_arr, comps, swaps = algorithm_instance.sort(original_case.copy())
                print(f"{name:<15} | {test_id:<4} | {comps:<11} | {swaps:<8}")
            except Exception as e:
                print(f"{name:<15} | {test_id:<4} | ERRO: {e}")
            

if __name__ == "__main__":
    main()