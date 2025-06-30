def quick_sort(arr):
    # Base case: stop recursion when low >= high
    def quicksort(arr, low, high):
        if low < high:
            # Partitioning the array using a determined pivot (at index high)
            pivot_index = partition(arr, low, high)
            # Recursively sorting the left partition
            quicksort(arr, low, pivot_index - 1)
            # Recursively sorting the right partition
            quicksort(arr, pivot_index + 1, high)

    # Helper function to partition the array using a determined pivot (at index high)
    def partition(arr, low, high):
        # Choosing the high index for the pivot (determined)
        pivot = arr[high]
        # Initialize the pointer for elements less than the pivot
        i = low - 1
        # Iterate through the array to rearrange/sort elements
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                # Swap elements to place smaller elements before the pivot
                arr[i], arr[j] = arr[j], arr[i]
        # Place the pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    # Test cases

    print("--- Quick Sort ---\n")

    # Random array
    random_array = [13, 41, 34, 21, 5, 19, 12]
    print(f"Testing on Random array: {random_array}")
    output_arr = quick_sort(random_array)
    print(f"Output = {output_arr}\n")

    # Sorted array
    sorted_array = [5, 12, 13, 19, 21, 34, 41]
    print(f"Testing on Sorted array: {sorted_array}")
    output_arr = quick_sort(sorted_array)
    print(f"Output = {output_arr}\n")

    # Reverse-sorted
    reverse_sorted_array = [41, 34, 21, 19, 13, 12, 5]
    print(f"Testing on Reverse-Sorted array: {reverse_sorted_array}")
    output_arr = quick_sort(reverse_sorted_array)
    print(f"Output = {output_arr}\n")