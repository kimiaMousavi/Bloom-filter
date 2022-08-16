import imp
from math import floor
from counting_bloom_filter import counting_bloom_filter
from random import shuffle
from leader_election import leader_election

import random
import string

item_count = 20 # no of items to add
n = 7 # size of the each counter
m = 150 # total number of the buckets
hash_count = 5 # number of hash functions
node_count = 500 #number of nodes


def id_generator(chars=string.ascii_uppercase, digits= string.digits ):
    return ''.join(random.choice(chars) + random.choice(digits))

id_list =[]
for i in range(node_count):
    id_list.append(id_generator())


counting_bloom_filter = counting_bloom_filter(item_count, n, m, hash_count)
print("Size of bit array:{}".format(counting_bloom_filter.m))
print("Size of each bucket:{}".format(counting_bloom_filter.N))
print("Number of hash functions:{}".format(counting_bloom_filter.k))

new_list = []
for item in id_list:
    counting_bloom_filter.add(item)

for word in id_list:
  if counting_bloom_filter.check(word):
    prob = round(counting_bloom_filter.check(word)[1]/(n*m) , 3) 
    print("'{}' is probably present ".format(word) + "and the is probably is '{}'!".format(prob))
    if (word, prob) not in new_list:
        new_list.append((word, prob))

  else:
    print("'{}' is definitely not present!".format(word))

leader_election = leader_election(new_list)
print(leader_election.select_leader())


