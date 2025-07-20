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
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        x = 1  # start from second element, since min_price is prices[0]
        while x < n:
            if prices[x] < min_price:
                min_price = prices[x]
            else:
                profit = prices[x] - min_price
                max_profit = max(max_profit, profit)
            x += 1

        if max_profit < 0:
            return 0

        return max_profit


# @leet end
