
def permute(s):
    out = []    
    # Base Case
    if len(s) == 1:
        out = [s]        
    else:
        # For every letter in string
        for i, char in enumerate(s):
            print char
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                print "  " + perm
                # Add it to output, also can use
                # extend() instead of +=
                out += [char + perm]
                # In the console out, this is the list
                # we iterate through in the 2nd for loop
                # so permute('bc') returns ['bc', 'cb']
                print "    ", out
    return out

def perms(s):
    result = []
    if len(s) == 1:
         return [s]
    for i,c in enumerate(s):
        result += [c+p for p in perms(s[:i]+s[i+1:])]
    return result

"""
RUN THE CODE BELOW TO TEST YOUR SOLUTION.
"""

class TestPerm(object):
    
    def test(self,solution):
        
        assert sorted(solution('abc')) == sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        assert sorted(solution('dog')) == sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])
        
        print 'All test cases passed.'
        


# Run Tests
t = TestPerm()
t.test(permute)