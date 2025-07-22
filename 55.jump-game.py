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
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        i = 0
        while i < len(nums):

            jump = nums[i]
            if i + jump >= len(nums) - 1:
                return True

            best = 0
            next_i = i

            for j in range(i + 1, i + jump + 1):
                if j < len(nums) and j + nums[j] > best:
                    best = j + nums[j]
                    next_i = j

            if next_i == i:
                return False

            i = next_i


# @leet end
