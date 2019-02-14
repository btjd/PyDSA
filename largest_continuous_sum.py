def lcs(arr):
    curr_sum = arr[0]
    max_sum = float('-inf')
    i = 1
    while i < len(arr):
        if arr[i] > curr_sum + arr[i]:
            curr_sum = arr[i]
        else:
            curr_sum += arr[i]
        if max_sum < curr_sum:
            max_sum = curr_sum
        i += 1
    return max_sum

class LargeContTest(object):
    def test(self,sol):
        assert sol([-2,-3,4,-1,-2,1,5,-3]) == 7
        assert sol([1,2,-1,3,4,-1]) == 9
        assert sol([1,2,-1,3,4,10,10,-10,-1]) == 29
        assert sol([-1,1]) == 1
        print 'ALL TEST CASES PASSED'
        
#Run Test
t = LargeContTest()
t.test(lcs)