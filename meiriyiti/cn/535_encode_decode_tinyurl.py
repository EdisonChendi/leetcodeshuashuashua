from random import random
import unittest
from typing import List
from pprint import pprint
import string 

class Codec:
    def __init__(self) -> None:
        self.codes = string.ascii + string.digits
        self.ls = {}
        self.sl = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.ls:
            return self.ls[longUrl]
        while True:
            short = "".join([random.choice(self.codes) for _ in range(6)])
            if short not in self.sl:
                self.sl[short] = longUrl
                self.ls[longUrl] = short
                return short
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.sl.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
