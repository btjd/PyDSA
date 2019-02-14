def anagram(s1,s2):
    buff = {}
    s1_list = list(s1)
    s2_list = list(s2)
    for e in s1_list:
        if e == ' ':
            continue
        elif e not in buff:
            buff[e] = 1
        else:
            buff[e] += 1
    for i in range(len(s2_list)):
        if s2_list[i] == ' ':
            continue
        elif buff[s2_list[i]] > 0:
            buff[s2_list[i]] -= 1
        else:
            return False
    for v in buff.values():
        if v != 0:
            return False
    return True


class AnagramTest(object):
    
    def test(self,sol):
        assert sol('go go go','gggooo') is True
        assert sol('abc','cba') is True
        assert sol('hi man','hi     man') is True
        assert sol('aabbcc','aabbc') is False
        assert sol('123','1 2') is False
        # assert sol('aa', 'bb') is False
        print "ALL TEST CASES PASSED"

# Run Tests
t = AnagramTest()
t.test(anagram)