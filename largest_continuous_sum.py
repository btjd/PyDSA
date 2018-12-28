def large_cont_sum(arr):
    lcs = s = arr[0]
    for item in arr[1:]:
        if (s + item) > item:
            s += item
        else:
            s = item
        if lcs < s:
            lcs = s
        print s, lcs
    return lcs



class LargeContTest(object):
    def test(self,sol):
        assert sol([-2,-3,4,-1,-2,1,5,-3]) == 7
        assert sol([1,2,-1,3,4,-1]) == 9
        assert sol([1,2,-1,3,4,10,10,-10,-1]) == 29
        assert sol([-1,1]) == 1
        print 'ALL TEST CASES PASSED'
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)