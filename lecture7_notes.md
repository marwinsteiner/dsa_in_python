# Linear Search and Binary Search

We will now focus on sorting algorithms like linear search, binary search, depth-first search, and breadth-first search.

## Searching Algorithms

- Searching for an element in a data structure is an essential operation
    - There are several ways to do it
- Algorithms that search for an element within a colelction
    - Linear search
    - Binary search

## Linear Search

- Tries to search for an element by looking at each element in the List.
- If the element is found, the algorithm stops and returns the result
- Otherwise, the algorithm continues.
- Has time complexity? (O(n))

### Implementation

```python
def linear_search(unordered_list, search_value):
    for index in range(len(unordered_list)):
        if unordered_list[index] == search_value:
            return True
    return False
```

Linear search has a time complexity of O(n). We can improve on this time complexity by using binary search.

## Binary Search

- Only applies to ordered lists
- Works by comparing the `search_value` with the item in the middle of the list, which we identify by labeling the first
  and last elements in the list. Let's say `search_value = 15`
- If we have a list of `integers = [2, 5, 10, 12, 15, 17, 20]`, binary search will label the first an last values as 2
  and 20, and look at the middle value, which is 12. 12 is not the `search_value`. 12 is smaller than the
  `search_value`, so we look at the right half of our list, numbers 15, 17, and 20. The first value is 15, the last
  value is 20, the middle value is 17. 17 is not our search value, and it is bigger than our search value, so we look to
  the left of 17 and find the number 15, which his both the first, last, and middle value. Since 15 equals the search
  value, we return True and the loop stops.

We can express this in code as follows

```python
def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if search_value == ordered_list[middle]:
            return True
        elif search_value < ordered_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False
```

The time complexity of binary search is O(log(n)), which is a lot better than O(n), especially when the size of the list
is big.