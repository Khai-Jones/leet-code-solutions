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
    def myAtoi(self, s: str) -> int:

        # Ignore whitespace
        s = s.strip()

        sign = ""
        # Detect and store sign
        if s and (s[0] == "-" or s[0] == "+"):
            sign = s[0]
            s = s.replace(s[0], "", 1)

        output = ""
        # check if number is int
        for char in s:
            if char.isdigit():
                output += char
            else:
                break

        int_min = -(2**31)
        int_max = 2**31 - 1

        if output == "":
            return 0
        if int(sign + output) < int_min:
            return int_min
        if int(sign + output) > int_max:
            return int_max
        return int(sign + output)


# @leet end
