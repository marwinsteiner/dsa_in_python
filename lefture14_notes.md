# Quicksort

Follows the divide and conquer principle. Implemented by many programming languages. Uses a partition technique by
choosing an element from the list, called the pivot. All items smaller than the pivot will end at the left of the pivot.
All elements greater end up on the right. Quicksort will be called recursively on the elements to the left and right of
the pivot.

We start with our collection of elements and follow Hoare's partition approach. It sets the pivot as the first element.
We use two pointers, the left pointer points to the immediately next consecutive element in the list, and the right
pointer points to the last item in the list. Hoare's partition approach says, to move the left pointer until a value
greater than the pivot is found. Then continue with the right pointer and move it until a value lower than the pivot is
found. As soon as this is the case, swap the items to which the pointers point. Again, we move the left pointer to the
right and stop when we find an element whose value is greater than the pivot. Move the right pointer to the left until
you again find a smaller value than the pivot. The pointers can visit elements which the other pointer has already
visited. Then let's say the pivot moves somewhere to the middle of the list, with elements on the right hand side
greater than the pivot and elements on the left hand side smaller than the pivot. We then recursively apply quicksort to
both sides of the list. When you recursively apply quicksort to both sides of a pivot, you apply a new pivot on the
left-most slice being sorted, and move the pivot to the right until, as a result of the quicksort, the numbers are
sorted.

## Implementation

```python
def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
        partition_index = partition(my_list, first_index, last_index)
        quicksort(my_list, first_index, partition_index)
        quicksort(my_list, partition_index + 1, last_index)


def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index
    while True:
        while my_list[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1
        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            left_pointer -= 1
        if left_pointer >= right_pointer:
            break
        my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]
    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    return right_pointer
```

Quicksort has a time complexity of O(n^2) in the worst case, and O(nlogn) in the average and best cases, as well as a
space complexity of the same amount.