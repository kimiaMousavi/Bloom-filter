# Leader Election with Bloom Filter

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

A Bloom Filter is a space-efficient probabilistic data structure, that is used to test whether an element is a member of a set.
The Counting Bloom filter allows approximating the number of times each element has been seen in the filter by incrementing the corresponding counter every time the element is added. This data structure contains a bit array and the array of counters. When a new element is inserted first compute its corresponding bit-positions, then increment the associated counter.
So we can use this probabilistic data structure to break the symmetry among nodes to select a leader.

	
## Technologies
Project is created with:
* Python3 
	
## Setup
To run this project you need python3 and then execute following code:

```
$ python3 example.py
```
