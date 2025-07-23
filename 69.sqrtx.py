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
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x

        if x < 2:
            return x

        while start <= end:
            mid = (start + end) // 2
            square = mid * mid

            if square == x:
                return mid
            if square < x:
                start = mid + 1
            else:
                end = mid - 1

        return end


# @leet end
