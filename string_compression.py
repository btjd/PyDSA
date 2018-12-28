def compress(s):
    """
    cc: current character
    ccc: current character count
    fs: final string
    """
    if len(s) == 0:
        return ''
    cc = s[0]
    ccc = 1
    fs = cc + str(ccc)
    for l in s[1:]:
        if l == cc:
            ccc += 1
            fs = fs[:-2]
            fs += cc + str(ccc)
        else:
            cc = l
            ccc = 1
            fs += cc + str(ccc)
    return fs

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestCompress(object):

    def test(self, sol):
        assert sol('') == ''
        assert sol('AABBCC') == 'A2B2C2'
        assert sol('AAABCCDDDDD') == 'A3B1C2D5'
        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestCompress()
t.test(compress)