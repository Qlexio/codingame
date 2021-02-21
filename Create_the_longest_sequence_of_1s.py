import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()

bit_list = []
bit_str = ""

# Split string by bit value
for num, i in enumerate(b):
    if bit_str == "":
        bit_str += i
    elif bit_str[-1] == i:
        bit_str += i
    else:
        bit_list.append(bit_str)
        bit_str = i
    
    if num == len(b) - 1:
        bit_list.append(bit_str)

total = 0

if len(bit_list) == 1 and "0" in bit_list[0]:
    total = 1
elif len(bit_list) == 1 and "1" in bit_list[0]:
    total = len(bit_list[0])
else:
    for num, i in enumerate(bit_list):
        if num == 0 and "0" in i:
            if 1 + len(bit_list[num + 1]) > total:
                total = 1 + len(bit_list[num + 1])
        elif num == len(bit_list) - 1 and "0" in i:
            if 1 + len(bit_list[num - 1]) > total:
                total = 1 + len(bit_list[num - 1])
        else:
            if "0" in i and len(i) == 1:
                if 1 + len(bit_list[num - 1]) + len(bit_list[num + 1]) > total:
                    total = 1 + len(bit_list[num - 1]) + len(bit_list[num + 1])
            elif "0" in i and len(i) > 1:
                if 1 + len(bit_list[num - 1]) > total:
                    total = 1 + len(bit_list[num - 1])
                elif 1 + len(bit_list[num + 1]) > total:
                    total = 1 + len(bit_list[num + 1])

print(total)