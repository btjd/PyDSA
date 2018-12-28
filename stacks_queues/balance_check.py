from stack import Stack
def balance_check(arr):
    #Edge case
    if len(arr)%2 != 0:
        return False
    opener = '[({'
    closer = '])}'
    s = Stack()
    for c in arr:
        # If the stack is empty at any point
        # push to it regardless
        if not s.isempty():
            top = s.peek()
            if c in closer and top in opener:
                # If top is opener and c is closer and
                # they match, we pop the top
                if opener.index(top) == closer.index(c):
                    s.pop()
                else:
                    # c is a closer and top is an opener
                    # but they don't match
                    s.push(c)
            else:
                # Being here means c is in opener
                # then we always push it regardless
                s.push(c)
        else:
            s.push(c)
    return s.isempty()

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert sol('[](){([[[]]])}(') == False
        assert sol('[{{{(())}}}]((()))') == True
        assert sol('[[[]])]') == False
        assert sol('{{([][])}()}') == True
        assert sol('[{()]') == False
        print 'ALL TEST CASES PASSED'
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)