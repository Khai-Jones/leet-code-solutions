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
    def reverse(self, x: int) -> int:
        str_x = str(x)
        min_range = -(2**31)
        max_range = 2**31 - 1

        sign = ""
        if str_x[0] == "-":
            sign = str_x[0]
            str_x = str_x[1:]

        rev = "".join(reversed(str_x))

        if int(sign + rev) < min_range or int(sign + rev) > max_range:
            return 0

        return int(sign + rev)


# @leet end
