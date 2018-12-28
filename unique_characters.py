def uni_char1(s):
    cnt = {}
    for c in s:
        if c not in cnt:
            cnt[c] = 1
        else:
            cnt[c] += 1
    for k in cnt:
        if cnt[k] > 1:
            return False
        else:
            return True

def uni_char(s):
    cnt = {}
    for c in s:
        if c not in cnt:
            cnt[c] = None
        else:
            return False
    return True

class TestUnique(object):

    def test(self, sol):
        # assert sol('') is True
        assert sol('goo') is False
        assert sol('abcdefg') is True
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char)