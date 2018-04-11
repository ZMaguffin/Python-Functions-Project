# Python-Functions-Project



This assignment simulates life in the real world, specifically at your first job.  You’ve been hired by IQ Software as a new software engineer working on the company’s main product.  Unfortunately for you, all of the development is done in Python, and you have been programming in Java and C++.  However, being a quick study and wanting to impress your new employer, you assure them that picking up Python won’t be a problem and won’t set you back more than a week or so, since it’s similar to other imperative languages you know.  Your employer points you to the Python web site, http://www.python.org, and suggests that you go through one of the tutorials there to begin to get familiar with the language.

 

Your assignment is to go through one or more of the Python tutorials, and then to write programs to do the following tasks in Python:

 

1.    To get warmed up, write a function, hlbackwards, that takes a list as input, and returns a list in which the elements of the toplevel list are in reverse order.  Here is a sample execution:

>>> hlbackwards([1,[2,3],[[4,5,[6],7],8,9]])

[[[4, 5, [6], 7], 8, 9], [2, 3], 1]

 

2.    To continue warming up, write a function, llbackwards, that takes a list as input, and returns a list in which every list and sublist is in reverse order.  Here is a sample execution:

>>> llbackwards([1,[2,3],[[4,5,[6],7],8,9]])

[[9, 8, [7, [6], 5, 4]], [3, 2], 1]

 

3.    Write a function, palindrome, that takes a list as input and returns the list if the list is a palindrome, ie reads the same in both directions, and otherwise returns the original list made into a palindrome by reversing it and appending it to itself, but not replicating the last element.  Here is a sample execution:

>>> palindrome([1,2,3,[2],1])

[1,2,3,[2],1,[2],3,2,1]

>>> palindrome([1,[2,3,[4]],[[4],3,2],1])

[1,[2,3,[4]],[[4],3,2],1]

 

4.    Write a function, permutations, that takes a list as input and generates a list containing all possible permutations of the list elements.  Here is a sample execution:

>>> permutations([1,2,3])

[[1, 2, 3], [1, 3, 2], [2, 3, 1], [2, 1, 3], [3, 1, 2], [3, 2, 1]]

 

5.    Write a function, ionah, that takes a single number as input and prints out the solution to the inverted disk problem for that many disks.  This is the problem of moving a stack of k disks of increasing size from bottom to top, from the first peg to the third peg with another peg that may be used as well, subject to the condition that a smaller disk is never put on top of a larger one, and only one disk may be moved at a time.  Here is a sample execution:

>>> ionah(3)

Move disk from peg  1  to peg  3

Move disk from peg  1  to peg  2

Move disk from peg  3  to peg  2

Move disk from peg  1  to peg  3

Move disk from peg  2  to peg  1

Move disk from peg  2  to peg  3

Move disk from peg  1  to peg  3

 

6.    Write a function, sequence, that takes a single integer as input and prints out a list containing that many terms of the sequence defined by

 

 

 

Here is a sample exection:

>>> sequence(7)

[0,1,2,5,12,29,70]

 

7.    Write a program to argue with yourself.  Your program should take statements that are typed in as a list and change the pronouns and negate them.  For instance, you should change to I, are should change to am not, and so on. 

 

Notice that bad things can happen if the input is not chosen carefully (for instance, you are too becomes I am not too).  Try to cover as many standard English patterns as you can to minimize the cases in which nonsense is returned.

 

Here is a sample run:

>>> argue(['you','are','a','stupid','computer'])

['i', 'am', 'not', 'a', 'stupid', 'computer']

>>> argue(['you','are'])

['i', 'am', 'not']

>>> argue(['are'])

   
['am', 'not']

>>> argue(['I', 'am', 'a', 'smart', 'human'])

['you', 'are', 'not', 'a', 'smart', 'human']

>>> argue(['your', 'mother', 'does', 'wear', 'army', 'boots'])

['my', 'mother', 'does', 'not', 'wear', 'army', 'boots']

>>> argue(['you', 'are', 'argumentative'])

['i', 'am', 'not', 'argumentative']

 

8.    Write a function, bubblesort, that takes a list of numbers as input and returns the list sorted in ascending order using a bubblesort.  Here is the output from a sample run:

>>> bubblesort([1,4,2,8,6,7])

[1, 2, 4, 6, 7, 8]
