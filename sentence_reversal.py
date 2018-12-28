def rev_word1(a):
    s = []
    a_list = a.split()
    for i in range(len(a_list)-1, -1, -1):
        s.append(a_list.pop())
        print(s)
    return ' '.join(s)

def rev_word(a):
    words = []
    i = 0
    while i < len(a):
        if a[i] != ' ':
            wsi = i
            while i < len(a) and a[i] != ' ':
                i += 1
            words.append(a[wsi:i])
        i += 1
    print(words)
    return ' '.join(reversed(words))
            

class ReversalTest(object):
    
    def test(self,sol):
        assert sol('    space before') == 'before space'
        assert sol('space after     ') == 'after space'
        assert sol('   Hello John    how are you   ') == 'you are how John Hello'
        assert sol('1') == '1'
        print "ALL TEST CASES PASSED"
        
# Run and test
t = ReversalTest()
t.test(rev_word)