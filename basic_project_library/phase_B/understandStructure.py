

import os
print(os.getcwd())

import sys
sys.path.append(os.path.dirname(__file__))


print(vars())
from growing_module import fun

fun()