# Merge Sort

Follows the divide and conquer technique, effectively dividing the big problem into smaller problems, and the smaller
sub-problems are solved recursively, then combine the solutions of the subproblems to achieve the final solution.

## Merge Sort - In Action

Merge sort takes a collection of integers, for instance, and divides this big collection into smaller collections
recursively, until it is left with collections which only contain one item, so a number of collections equal to the
number of elements in the collection you started with. These individual collections are then combined in ascending order
into a new set of collections.

### Implementation
```python
def merge_sort(my_list):
    if len(my_list) > 1:
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
            while i < len(left_half):
                my_list[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                my_list[k] = right_half[j]
                j += 1
                k += 1
```

In the best, worst, and average case, merge sort has a time complexity of O(nlogn), which is a significant improvement over bubble sort, selection sort, and insertion sort.

Other algorithms, for example bubble sort or insertion sort have better best case complexity.

Merge sort has a space complexity of O(n).