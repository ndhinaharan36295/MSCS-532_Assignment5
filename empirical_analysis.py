import random
from randomized_quick_sort import randomized_quick_sort
from quick_sort import quick_sort
import time
import sys
from tabulate import tabulate

sys.setrecursionlimit(6000)

if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000]

    # Analysis on Random array
    print(f"\n--- Analysis on Random arrays ---\n")
    results = []
    for size in sizes:
        input_array = [random.randint(1, 10000) for _ in range(size)]

        start_time = time.time()
        quick_sort(input_array)
        quick_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{quick_sort_time:.2f} ms", f"{randomized_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Deterministic Quick Sort", "Randomized Quick Sort"], tablefmt="grid"))


    # Analysis on Sorted array
    print(f"\n--- Analysis on Sorted arrays ---\n")
    results = []
    for size in sizes:
        input_array = list(range(size))

        start_time = time.time()
        quick_sort(input_array)
        quick_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{quick_sort_time:.2f} ms", f"{randomized_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Deterministic Quick Sort", "Randomized Quick Sort"], tablefmt="grid"))

    # Analysis on Reverse sorted array
    print(f"\n--- Analysis on Reverse Sorted arrays ---\n")
    results = []
    for size in sizes:
        input_array = list(range(size, 0, -1))

        start_time = time.time()
        quick_sort(input_array)
        quick_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{quick_sort_time:.2f} ms", f"{randomized_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Deterministic Quick Sort", "Randomized Quick Sort"], tablefmt="grid"))

