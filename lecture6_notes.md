# Recursion

## Definition

- Function calling itself
- almost all the situations where we use loops
    - Substitute the loops using recursion
- Can solve problems that seem very complex at first

## Example - factorial

The factorial of an integer number is written as follows:
$$n! = n \times (n-1) \times (n-2) \times \dots \times 1$$

For example, the factorial of 5 would be written as:
$$5! = 5\times4\times3\times2\times1 = 120$$

We can implement the factorial of a number with the following code:

```python
def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result
```

Using this function, `factorial(5)` returns 120.

## Example - factorial using recursion

$$n! = n \times (n-1)!$$

Which we can implement as follows:

```python
def factorial_recursion(n):
    return n * factorial_recursion(n - 1)
```

But this would result in infinite recursion, it would run forever.

## Example - identifying the base case

To fix the issue of infinite recursion, we should identify the base-case, which is to say, add a condition to ensure
that our algorithm doesn't execute forever.

In our example, the base case of the factorial operator, is when $n = 1$.

Hence, we can improve our function:

```python
def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)
```

## How Recursion Works

When using recursion, the computer uses a stack to keep track of the functions. This step is called the call stack. In
the factorial example we saw when we called `factorial(5)`, the program did not finish when it had called that, it
actually also called `factorial(4)`. This is because it pushed `factorial(5)` to the call stack. It happens the same way
with the rest of the calls. `factorial(1)` finishes without any recursion call and returns 1, which is what
`factorial(2)` receives. The execution of `factorial(2)` continues. When `factorial(2)` finishes, it returns 2,
because $2 \times 1 = 2$, and the item is popped from the stack. It happens the same way for the rest of the items in
the calls.

## Dynamic Programming

Dynamic programming is an optimization technique mainly applied to recursion. It can reduce the complexity of recursive
algorithms. It can be used for any problem that can be divided into smaller subproblems which overlap. Solutions of the
subproblems are saved, avoiding the need to recalculate, using the memoization technique.