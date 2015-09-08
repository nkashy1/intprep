# intprep

Coding interview preparation

- - -

### September 8, 2015

I am currently looking for jobs and have been for the past ten days or so. This repository contains a large portion of my interview preparation. I doubt anyone is ever going to read this as I am not really putting it out there, but the repository is as much for my own benefit so that I have a decent amount of data off of which I can estimate my
vulnerabilities.

To start with, I had a couple of phone screens last week and have follow-up phone interviews this week, where I will be expected to code. If these interviews go well, I will be called in for live interviews.
After my first phone screen, I realized that I would need to put some effort into understanding the interview meta-game. I immediately ordered [Cracking the Coding Interview](http://www.amazon.com/Cracking-Coding-Interview-6th-Edition/dp/0984782850) by Gayle Laakmann McDowell. This is my major source of information, supplemented by various blog posts, web sites, and study guides sent to me by recruiters. Everything I have read seems consistent with the information presented by McDowell in her book.

While waiting for the book to get here, I solved some problems from [HackerRank](https://www.hackerrank.com/). You can find my solutions in the [hackerrank](./hackerrank/) directory. I also solved the [Fizzbuzz](https://github.com/nkashy1/intprep/blob/master/fizzbuzz/fizzbuz.py) problem as a sort of sanity check.

McDowell presented a great table towards the beginning of her book about the stuff that you absolutely *need* to know before an interview. Markdown isn't particularly table-friendly, so I will use a different format.

##### Data Structures

1. Linked lists

2. Trees, Tries, Graphs

3. Stacks and Queues

4. Heaps

5. Vectors/ArrayLists

6. Hash Tables


##### Algorithms

1. Breadth-first search

2. Depth-first search

3. Binary search

4. Merge sort

5. Quick sort


##### Concepts

1. Bit manipulation

2. Memory (stack vs. heap)

3. Recursion

4. Dynamic programming

5. Algorithmic analysis -- running time and space


Additionally, one big vulnerability in all of this is your ability to communicate with your interviewer *during* the problem-solving process. This is certainly my greatest exposure to the risk of failure in the interview process, as I like to work on problems in solitude.

Once I did get McDowell's book, I got all gung-ho about solving the problems and decided that I was going to go sequentially through all the problems in her book, writing down the solution to each one in a notebook, talking out loud through each one as I went. It actually went remarkably well for a week or so. Starting in Chapter 2, I also started implementing all of the solutions in Python and pushing them to the [crack](./crack/) directory of this repository. The file names reflect McDowell's problem numbering.

With the phone interviews drawing closer upon me, though, I think I'll cool it on the sequential solution of the McDowell problems. I have the following vulnerabilities that I still need to work on (in order of priority):

1. Tries

2. Hash tables

3. Merge sort

4. Quick sort

5. Dynamic programming

6. Bit manipulation


For the first four, my vulnerability is that, although I have a good idea how to use the structures and algorithms in question, I have not yet written implementations. I will rectify that today.

For the concepts -- dynamic programming and bit manipulation -- I will be reading the relevant chapters of McDowell's book and solving some problems from those chapters. This will probably happen tomorrow.


##### After the phone interviews

All this preparation is just the minimal amount of preparation recommended by McDowell and probably won't suffice beyond the initial phone screen. Starting this Saturday, I will need to take things to the next level in terms of preparation. The following is a list of topics that I think I'll have to brush up on:

1. Djikstra's algorithm (implement)

2. Collision resolution in hash tables (test against custom hash table implementation)

3. Scalability (chapter from McDowell's book)

4. A\* search (implement)

5. Regression (least squares derivation in in 2 dimensions, then the general case)

6. Minimax (implement)


I will be using McDowell's book, Russell and Norvig, and Wikipedia.

- - -