from tkinter.tix import Balloon
import unittest
from typing import List
from pprint import pprint

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance[:]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            else:
                self.deposit(account1, money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid_acount_num(account):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid_acount_num(account) or not self.enough(account, money):
            return False
        self.balance[account-1] -= money
        return True

    def valid_acount_num(self, account:int) -> bool:
        return 1 <= account <= len(self.balance)
    
    def enough(self, account:int, money:int) -> bool:
        return self.balance[account-1] >= money


# class TestSolution(unittest.TestCase):

#     def test_case_1(self):
#         sol = Solution()
#         pass
        
#     def test_edge_case_1(self):
#         sol = Solution()


if __name__ == "__main__":
    unittest.main()
