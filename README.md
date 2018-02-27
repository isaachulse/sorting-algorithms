# Sorting Algorithms

    ____                         __  __      __
   /  _/________ _____ ______   / / / /_  __/ /_______
   / // ___/ __ `/ __ `/ ___/  / /_/ / / / / / ___/ _ \
 _/ /(__  ) /_/ / /_/ / /__   / __  / /_/ / (__  )  __/
/___/____/\____/\____/\___/  /_/ /_/\____/_/____/\___/


Running Example PYTHON / BASH

To run, select either 'bubble', 'quick' or 'selection' sorts and add as first element in argument to pass,
add any number of arguments afterwards: int format [e.g. 5, 6, 12]; float format [e.g. 3.0, 12.56, 1.674] or
string format [e.g. '124.89', 'foo', 'bar123']. The terminal will print the sorted results. 

Bubble Sort:

    PYTHON  >>> bubble_sort([<mixed list>])

    BASH    $ python sorting_algorithms.py bubble arg1 arg2 arg3 argn

      e.g.  $ python sorting_algorithms.py bubble 32 '234' 12.45 '3245.12'
   
        returns: [12.45, 32.0, 234.0, 3245.12]

-----------------------------

Quick Sort:

    PYTHON  >>> quick_sort([<mixed list>])

    BASH    $ python sorting_algorithms.py quick arg1 arg2 arg3 argn

      e.g.  $ python sorting_algorithms.py bubble 25 '26.21' '19.5' 'asdf'

        returns: [19.5, 25.0, 26.21]

-----------------------------

Selection Sort:

      PYTHON  >>> selection_sort([<mixed list>])

      BASH    $ python sorting_algorithms.py selection arg1 arg2 arg3 argn

      e.g.  $ python sorting_algorithms.py bubble 'foo' 8 '47bar' 0.234

        returns: [0.234, 8.0]

-----------------------------

Unit Testing

To run, select use command below, which finds all unit tests in directory. Please see
test_sorting_algorithms.py for details on unit tests. 

      BASH    $ python -m unittest discover

-----------------------------

  
  Expected:
	
	----------------------------------------------------------------------
	Ran 11 tests in 0.001s

	OK

-----------------------------
