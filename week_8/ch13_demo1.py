# CMPT 141 - Arrays
# Topic(s): Arrays VS Lists
# DEMO


import numpy as np
import time as time
import sys as sys

def compare_sequences( N ):
    """
    prints wall clock time to sum array vs list of identical values
    also prints memory use of array vs list
    N: amount of data items in sequences
    """
    # generate N numbers in the range [0,N-1] & store them in list & array
    l = list(range(N))  # list of N numbers
    a = np.arange(N)    # array of N numbers

    # print the time taken to sum each sequence
    # sum list
    t_start = time.time()
    sum(l)
    l_time = time.time() - t_start
    # sum array
    t_start = time.time()
    np.sum(a)
    a_time = time.time() - t_start

    print("Sum Time via sum() (List):",l_time,"s")
    print("Sum Time via np.sum() (Array):",a_time,"s")

    # print the memory used
    print("Memory Used By List:",sys.getsizeof(l),"bytes")
    print("Memory Used By Array:",sys.getsizeof(a),"bytes")

compare_sequences(10000000)
