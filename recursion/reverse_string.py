def reverse(s):
    """
    Return the reverse of an input string
    """
    def _reverse(s, ret):
        if s == '':
            return ''.join(ret)
        else:
            ret.append(s[-1])
            return _reverse(s[:-1], ret)
    ret = []
    return _reverse(s, ret)

'''
RUN THE CODE BELOW TO TEST YOUR SOLUTION.
'''

class TestReverse(object):
    
    def test_rev(self,solution):
        assert solution('hello') == 'olleh'
        assert solution('hello world') == 'dlrow olleh'
        assert solution('123456789') == '987654321'
        
        print 'PASSED ALL TEST CASES!'
        
# Run Tests
test = TestReverse()
test.test_rev(reverse)