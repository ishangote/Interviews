# Leetcode contest 198 Medium
"""
exchange_rate = 2, initial_full_bottles = 5

5
3
2
1

total_num = 11

exgr =  3  init_bots = 2 -> return 2
exgr =  3  init_bots = 10

drink = 10
empty = 4

drink = 14
empty = 2


exgr = 5  init_bots = 11

drink = 11 + 2 = 13

empty = 0
empty = 11  
empty = 11%5 + 11//5 = 3


exg = 3
curr_full = 1
empty = 2
ans = 0

Transaction :
while curr_full >= exg:
    ans += curr_full
    empty += curr_full
    curr_full = empty // exg
    empty = empty % exg
    
return (ans + curr_full)
    
"""
def num_bottles_drank(exg, curr_full):
    #Input validations...
    if exg < 2: return None
    
    ans, empty = 0, 0 
    while curr_full >= exg:
        ans += curr_full
        empty += curr_full
        curr_full = empty // exg
        empty = empty % exg
    
    return ans + curr_full
    
"""
exg = 3
curr_full = 1
empty = 1
ans = 7 + 1

Testcases
Input    Expected    Actual 
(2  1)     1           1
(2, 5)     8           8
"""

# REF: Water Bottles Leetcode
def exchange(empty_bottles, exchange_rate):
    if exchange_rate > empty_bottles: return False
    full_bottles = empty_bottles // exchange_rate
    empty_bottles = empty_bottles % exchange_rate
    return [full_bottles, empty_bottles]


def num_water_bottles(initial_full_bottles, exchange_rate):
    ans = initial_full_bottles
    empty_bottles = initial_full_bottles

    while True:
        excg = exchange(empty_bottles, exchange_rate)
        if not excg: return ans
        full_bottles, empty_bottles = excg[0], excg[1]
        ans += full_bottles
        empty_bottles += full_bottles

import unittest
class TestWaterBottles(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(num_water_bottles(9, 3), 13)
        self.assertEqual(num_water_bottles(13, 3), 19)

if __name__ == "__main__": unittest.main()