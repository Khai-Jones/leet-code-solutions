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
    def climbStairs(self, n: int) -> int:
        prev_val = {}

        def helper_func(n):

            if n in prev_val:
                return prev_val[n]
            if n == 1:
                return 1
            if n == 2:
                return 2

            prev_val[n] = helper_func(n - 1) + helper_func(n - 2)
            return prev_val[n]

        return helper_func(n)


# @leet end
