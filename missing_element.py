def finder(arr1,arr2):
    sum1 = 0
    sum2 = 0
    for e in arr1:
        sum1 += e
    for e in arr2:
        sum2 += e
    return sum1 - sum2

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestFinder(object):
    
    def test(self,sol):
        assert sol([5,5,7,7],[5,7,7]) == 5
        assert sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]) == 5
        assert sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) == 6
        print 'ALL TEST CASES PASSED'

# Run test
t = TestFinder()
t.test(finder)