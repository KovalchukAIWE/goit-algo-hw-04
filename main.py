import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tim_sort(arr):
    return sorted(arr)

def test_sorting_performance(sorting_function, arr):
    test_arr = arr.copy()
    return timeit.timeit(lambda: sorting_function(test_arr), number=1)

sizes = [1000, 5000, 10000, 50000, 100000]
results = {"Merge Sort": [], "Insertion Sort": [], "Timsort": []}

for size in sizes:
    random_list = [random.randint(0, 1000000) for _ in range(size)]
    
    merge_time = test_sorting_performance(merge_sort, random_list)
    insertion_time = test_sorting_performance(insertion_sort, random_list[:1000]) if size <= 1000 else None
    timsort_time = test_sorting_performance(tim_sort, random_list)

    results["Merge Sort"].append(merge_time)
    results["Insertion Sort"].append(insertion_time)
    results["Timsort"].append(timsort_time)

print("Sorting Algorithm Performance:")
print("Size\tMerge Sort\tInsertion Sort\tTimsort")
for i, size in enumerate(sizes):
    merge_res = f"{results['Merge Sort'][i]:.6f}" if results['Merge Sort'][i] is not None else "N/A"
    insertion_res = f"{results['Insertion Sort'][i]:.6f}" if results['Insertion Sort'][i] is not None else "N/A"
    timsort_res = f"{results['Timsort'][i]:.6f}" if results['Timsort'][i] is not None else "N/A"
    print(f"{size}\t{merge_res}\t{insertion_res}\t{timsort_res}")
