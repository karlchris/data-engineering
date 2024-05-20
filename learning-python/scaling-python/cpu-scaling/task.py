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
