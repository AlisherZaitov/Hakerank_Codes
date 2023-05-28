#If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    name =  int (input ())
    if name % 2:
        print("Weird")
    else:
        if 2 < name <= 5:
            print("Not Weird")
        elif 6 <name <= 20:
            print("Weird")
        elif 20 < name:
            print("Not Weird")
    
