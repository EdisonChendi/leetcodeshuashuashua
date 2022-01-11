import unittest
from typing import List
from pprint import pprint

from collections import deque

class MeetException(Exception):
    pass

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(source, target) -> bool:
            BOUNDARY = 10**6
            visited = {tuple(source),}
            q = deque([source])
            countdown = limit
            while q and countdown > 0:
                x, y = q.popleft()
                for nx, ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
                    if 0 <= nx < BOUNDARY and 0 <= ny < BOUNDARY and (nx,ny) not in blocked and (nx,ny) not in visited:
                        if [nx, ny] == target:
                            raise MeetException
                        visited.add((nx,ny))
                        q.append([nx, ny])
                        countdown -= 1
            return countdown <= 0

        if len(blocked) < 2:
            return True

        blocked = {tuple(b) for b in blocked}
        limit = len(blocked)*(len(blocked)-1)//2
        try:
            if bfs(source, target) and bfs(target, source):
                return True
        except MeetException:
            print("here!")
            return True
        else:
            return False

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        blocked = [[0,1],[1,0]]; source = [0,0]; target = [0,2]
        expected = False
        self.assertEqual(sol.isEscapePossible(blocked, source, target), expected)
        
    def test_case_2(self):
        sol = Solution()
        blocked = []; source = [0,0]; target = [999999,999999]
        expected = True
        self.assertEqual(sol.isEscapePossible(blocked, source, target), expected)

    def test_case_3(self):
        sol = Solution()
        blocked = [[100005,100073],[100006,100074],[100007,100075],[100008,100076],[100009,100077],[100010,100078],[100011,100079],[100012,100080],[100013,100081],[100014,100082],[100015,100083],[100016,100084],[100017,100085],[100018,100086],[100019,100087],[100020,100088],[100021,100089],[100022,100090],[100023,100091],[100024,100092],[100025,100091],[100026,100090],[100027,100089],[100028,100088],[100029,100087],[100030,100086],[100031,100085],[100032,100084],[100033,100083],[100034,100082],[100035,100081],[100036,100080],[100037,100079],[100038,100078],[100039,100077],[100040,100076],[100041,100075],[100042,100074],[100043,100073],[100044,100072],[100043,100071],[100042,100070],[100041,100069],[100040,100068],[100039,100067],[100038,100066],[100037,100065],[100036,100064],[100035,100063],[100034,100062],[100033,100061],[100032,100060],[100031,100059],[100030,100058],[100029,100057],[100028,100056],[100027,100055],[100026,100054],[100025,100053],[100024,100052],[100023,100053],[100022,100054],[100021,100055],[100020,100056],[100019,100057],[100018,100058],[100017,100059],[100016,100060],[100015,100061],[100014,100062],[100013,100063],[100012,100064],[100011,100065],[100010,100066],[100009,100067],[100008,100068],[100007,100069],[100006,100070],[100005,100071]]
        source = [100024,100072]
        target = [999994,999990]
        expected = True
        self.assertEqual(sol.isEscapePossible(blocked, source, target), expected)

    def test_case_4(self):
        sol = Solution()
        blocked = [[1,0],[1,1]]; source = [0,0]; target = [2,0]
        expected = True
        self.assertEqual(sol.isEscapePossible(blocked, source, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
