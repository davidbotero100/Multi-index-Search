# Multi-Index-Search

The intent of this search algorithm is to experiment with alternate implementations 
of search algorithms for unordered lists, following a similar approach to the divide-and-conquer method. 

However, this algorithm does not require recursion; it splits list into segments 
using pairs of indexes for each segment.

This algorithm has an initial number of indexes n = 8, thus the algorithm only works on lists 
equal or larger than 8 elements.

The segments and indexes are set dynamically based on list size to maintain efficiency.

Further improvements to follow: 
    Add stopping conditions if element not found
    Experiment different approaches


# Behaviour  

For a list of say 100 elements, the initial indexes are set as follows.

Initial indexes:
Segment 0: start_0 = 0, end_0 = 13
Segment 1: start_1 = 14, end_1 = 27
...
Segment 6: start_6 = 84, end_6 = 99

Then, for each iteration during the search, the start and end indexes 
of each segment close inwards on their respective segment as follows.

Segment 0: start_0 = 1, end_0 = 12
Segment 1: start_1 = 15, end_1 = 26
...
Segment 6: start_6 = 85, end_6 = 98

This process continues until the target is found or all segments close if the target is not found.


# Big-O

Since the list is divided into log(n) segments, the size of the largest segment is roughly n/log(n),
and if the element is not found, the algorithm overlaps each segment thereby doubling it, so we get 2log(n).

Therefore, this algorithm stands in O(n/2log(n)) thus far. Further improvements to be made. 
Aiming for O(nlog(n)) or O(log(n))