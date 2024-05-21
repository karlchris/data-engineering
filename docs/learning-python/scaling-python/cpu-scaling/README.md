# CPU Scaling

As CPUs are not getting infinitely faster, using multiple CPUs is the best path towards scalability.
That means introducing concurrency and parallelism into your program.

## Threads

Threads in Python are a good way to run a function concurrently with other functions.
If your system does not support multiple processors, the threads will be executed one after another as scheduled by the operating system.
However, if multiple CPUs are available, threads could be scheduled on multiple processing units, once again as determined by the operating system.

![Multi Threading](../pics/multi-threading.png)

```python
import threading

def print_something(something):
    print(something)

t = threading.Thread(target=print_something, args=("hello",))
t.start()
print("thread started")
t.join()
```

### Drawbacks

If you specifically expected any one of the outputs each time, then you forgot that there's no guarantee regarding the order of execution for the threads.
If you do not join all your threads and wait for them to finish, it is possible that the main thread finishes and exits before the other threads.
If this happens, your program will appear to be blocked and will not respond to even a simple `KeyboardInterrupt` signal.

### Threads as `daemons`

To avoid this, and because your program might not be in a position to wait for the threads,
you can configure threads as _daemons_. When a thread is a daemon, it's considered as a **background thread by Python** and is terminated as soon as the main thread exits.

```python
import threading

def print_something(something):
    print(something)

t = threading.Thread(target=print_something, args=("hello",))
t.daemon = True # Specifying as Daemon here
t.start()
print("thread started") # No longer a need to use the JOIN method
```

## Using `Processes`

Since multithreading is not a perfect scalability solution because of GIL,
using `processes` instead of threads is a good alternative.

`multiprocessing` library is a good, higher-level alternative. It provides an interface that starts new processes, whatever your operating system might be.
It also provides a _pool_ mechanism that is useful in more _functional_ manner.

```python
import multiprocessing
import random

def compute(n):
    return sum(
        [random.randint(1, 100) for i in range(1000000)])

if __name__ == "__main__":
    # Start 8 workers
    pool = multiprocessing.Pool(processes=8)
    print("Results: %s" % pool.map(compute, range(8)))
```

![image](../pics/multiprocessing.png)

## Challenge

- Follow below task and its solution.

=== "Task"

    ```python
    """
        Problem
            You are given a list of one million integers named mylist.

            However, since we have studied that parallelism can be used to utilize more cores of the CPU to compute the result faster we know that the simplest way to parallelize a program is to use use threads.

        One thing to keep in mind while using threads is that the tasks assigned to the threads should be independent of the task of other threads.
        In other words, you have to divide your problem into smaller non-overlapping chunks that can be done independently.

        Hint: A list can be divided into many partitions and the min of all the chunks can be computed separately.
        Then, the min of the computed mins of all chunks will be the global minimum.
    """

    # Relevant libraries are imported already
    import random
    import threading

    # mylist contains 1 million entries ranging from 1 to 100000000
    mylist = [random.randint(1, 100000000) for i in range(1000000)]
    minimum = 0
    ########
    # Your code goes here #


    #   Code until here   #
    ########

    # Result:
    print("Global Minimum: ", minimum)
    ```

=== "Solution"

    ```python
    """
        First of all the mylist can be divided into non-overlaping chunks.
        Then, the minimum of each chunk can be computed separately.
        We use threads to compute the minimum of each of the four chunks and store all four minimums in the mins list.
        Finally, we calculate the minimum of those four minimums which is the global minimum of the list.
    """

    import random
    import threading

    mylist = [random.randint(1, 100000000) for i in range(1000000)]
    mins = []

    def calc_min(li):
        minimum = li[0]
        for x in li:
            if x < minimum:
                minimum = x

        mins.append(minimum)

    # Dividing list in halves
    l1 = mylist[:len(mylist)//2]
    l2 = mylist[len(mylist)//2:]

    # Dividing list in quaters
    q1 = l1[:len(l1)//2]
    q2 = l1[len(l1)//2:]
    q3 = l2[:len(l2)//2]
    q4 = l2[len(l2)//2:]

    workers = []
    workers.append( threading.Thread(target=calc_min, args=(q1,)) )
    workers.append( threading.Thread(target=calc_min, args=(q2,)) )
    workers.append( threading.Thread(target=calc_min, args=(q3,)) )
    workers.append( threading.Thread(target=calc_min, args=(q4,)) )

    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

    print("Global Minimum: ", min(mins))
    ```

!!! tip

    This challenge is using `threads` as its simplest approach, if you want to challenge yourself further, you can try to use `multiprocessing` library, which I believe, it should be simpler and cleaner code.
