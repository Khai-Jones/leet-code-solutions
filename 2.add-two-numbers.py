# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *

# @leet imports end


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        node_head = ListNode(0)
        y = node_head

        def retrieve_num(x, output):

            output.append(x.val)
            x = x.next

            if x is None:
                return output

            return retrieve_num(x, output)

        output_l1 = retrieve_num(l1, [])
        output_l2 = retrieve_num(l2, [])

        output_l1.reverse()
        output_l2.reverse()

        output_l1 = int("".join(map(str, output_l1)))
        output_l2 = int("".join(map(str, output_l2)))

        total = output_l1 + output_l2
        output = [int(num) for num in str(total)]
        output.reverse()

        for number in output:
            y.next = ListNode(number)
            y = y.next

        return node_head.next


# @leet end
