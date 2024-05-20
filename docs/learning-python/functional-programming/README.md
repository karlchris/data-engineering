# Functional Programming in Python

A **pure function** is a function whose output value follows solely from its input values, without any observable side effects.
In **functional programming**, a program consists entirely of evaluation of pure functions. Computation proceeds by nested or composed function calls, without changes to state or mutable data.

## How it works

In functional programming, it's useful to have these 2 abilities:

- to take another function as an argument
- to return another function to its caller

This suits very well with Python as everything is **object**.

example

```python
def func():
    print("I am function func()!")

func()
# Output: I am function func()!

another_name = func
another_name()
# Output: I am function func()!
```

## Advantanges

- High level: You’re describing the result you want rather than explicitly specifying the steps required to get there. Single statements tend to be concise but pack a lot of punch.
- Transparent: The behavior of a pure function depends only on its inputs and outputs, without intermediary values. That eliminates the possibility of side effects, which facilitates debugging.
- Parallelizable: Routines that don’t cause side effects can more easily run in parallel with one another.

## Anonymous Function

Functional programming is all about calling functions and passing them around, so it naturally involves defining a lot of functions.
You can always define a function in the usual way, using the `def` keyword as you have seen.

Sometimes, though, it’s convenient to be able to define an **anonymous function** on the fly, without having to give it a name.
In Python, you can do this with a `lambda` expression.

```python
lambda <parameter list>: <expression>
```

example:

```python
reverse = lambda s: s[::-1]
reverse("I am a string")
# Output: 'gnirts a ma I'
```

## Applying Function to an Iterable with `map()`

`map()` is Python built-in function. With `map()`, you can apply a function to each element in an iterable in turn,
and `map()` will return an iterator that yields the results.

```python
map(<function>, <iterable>)
```

Example:

```python
def reverse(s):
    return s[::-1]

animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(reverse, animals)

for a in iterator:
    print(a)

# tac
# god
# gohegdeh
# okceg
```

## Selecting Elements from Iterable with `filter()`

`filter()` allows you to select or filter items from an iterable based on evaluation of the given function. It’s called as follows:

```python
filter(<f>, <iterable>)
```

filter(<f>, <iterable>) applies function <f> to each element of <iterable> and returns an iterator that yields all items for which <f> is truthy.

Example:

```python
def greater_than_100(x):
    return x > 100

list(filter(greater_than_100, [1, 111, 2, 222, 3, 333]))
# Output: [111, 222, 333]
```

## Reducing an Iterable to a Single Value with `reduce()`

`reduce()` applies a function to the items in an iterable two at a time, progressively combining them to produce a single result.

The most straightforward reduce() call takes one function and one iterable, as shown below:

```python
reduce(<f>, <iterable>)
```

reduce(<f>, <iterable>) uses <f>, which must be a function that takes exactly two arguments,
to progressively combine the elements in <iterable>.
To start, reduce() invokes <f> on the first two elements of <iterable>.
That result is then combined with the third element,
then that result with the fourth,
and so on until the list is exhausted. Then reduce() returns the final result.

```python
from functools import reduce


def f(x, y):
    return x + y


reduce(f, [1, 2, 3, 4, 5])
# Output: 15
```

## Challenge

- Follow on [Task](task.py) for the problem statement.
- Check [Solution](solution.py) for the solution.

Reference: [Functional Programming in Python](https://realpython.com/python-functional-programming/#what-is-functional-programming)
