# Bubble Sort

## Sorting Algorithms

- Deeply studied
- Solve how to sort an unsorted collection in ascending/descending order.
- Can reduce complexity of problems.
- Some sorting algorithms
    - Bubble sort
    - Selection sort
    - Insertion sort
    - Merge sort
    - Quick sort

## Bubble Sort

We take our collection of items and if:

- First value greater than the second value
    - Swap them
- Second value greater than the first value
    - Do nothing
- Keep iterating over the collection until the largest item bubbles to the end of the collection.

## Implementation

```python
def bubble_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        for j in range(list_length - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list
```

But what if we want to verify whether or not the list is already sorted before we run our sorting algorithm?

We can implement this as follows

```python
def bubble_sort(my_list):
    list_length = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(list_length - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                is_sorted = False
        list_length -= 1
    return my_list
```

## Bubble Sort - Complexity

Bubble sort has terrible time complexity! O(n^2). In our improved version, the time complexity reduces to O(n), because
we check if it's already sorted, removing the second "dimension" of sorting.

Bubble sort does not perform well with highly unsorted large lists. However, in the improved version it performs well if
the list is large and/or mostly sorted. 

