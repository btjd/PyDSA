def pair_sum(arr,k):
    buff = {}
    count = 0
    for i in range(len(arr)):
        print(buff)
        if arr[i] not in buff:
            buff[k - arr[i]] = i
        else:
            count += 1
        print(count)
    print(count)
    return count

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestPair(object):
    
    def test(self,sol):
        assert sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) == 6
        assert sol([1,2,3,1],3) == 1
        assert sol([1,3,2,2],4) == 2
        print 'ALL TEST CASES PASSED'
        
#Run tests
t = TestPair()
t.test(pair_sum)