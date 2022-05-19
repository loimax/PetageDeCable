#Trouver le nombre unique dans une liste de doublons

from itertools import count
from operator import xor
import time as t

R = 0
list = [7, 55, 8, 10, 1, 10, 78, 1, 8, 7, 55, 1000, 1000]

# option 1 avec des xor
for e in list:
    R = R ^ e
print(R)

# option 2 mais moins performante by moi
# i = 0
# while i < len(list) : 
#     x = list[i]
#     print(f"\033[1;31;40m Var X à tester : {x}\033[0m")
#     # t.sleep(1)

#     count_doubles = 0
#     for e in list:
#         print(f"count-doubles = {count_doubles}")
#         print(f"x = {x}, e = {e}\n")
#         if x == e and not count_doubles == 2 :
#             count_doubles += 1

#         elif count_doubles == 2 :
#             break

#         else :
#             continue
        
#     if count_doubles == 1 :
#         print(f"\n\nLe nombre unique est {x}")
#         break
#     i += 1
