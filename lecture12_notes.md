# Selection Sort and Insertion Sort

## Selection Sort

If we have a collection of integers, the selection sort looks at all the values in the collection, determining the
lowest value in the collection. Once we find the lowest value of the collection of integers, we swap this lowest value
with the first unordered element in the collection. Then we do n more sorts until the collection of integers is sorted
in ascending order.

### Implementation

```python
def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        lowest = my_list[i]
        index = i
        for j in range(i + 1, list_length):
            if my_list[j] < lowest:
                lowest = my_list[j]
        my_list[i], my_list[index] = my_list[index], my_list[i]
    return my_list
```

In the worst, average, and best case, selection sort has a time complexity of O(n^2).

## Insertion Sort

We again have a collection of integers. We compare the first two values. We shift the value which is bigger to the
right, and the value that is smaller, to the left. We continue by comparing elements at index 1 and 2, then 2 and 3,
each time shifting the bigger value to the right and the smaller value to the left.

### Implementation
```python
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        number_to_order = my_list[i]
        j = i - 1
        while j >= 0 and number_to_order < my_list[i]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = number_to_order
    return my_list
```

In the worst and average case, the time complexity of the insertion sort is O(n^2), but in the best case it is only O(n)