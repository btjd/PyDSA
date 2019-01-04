def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# print(fib_rec(10))

# Memoization using method as decorator
def memoize(f):
    memo = {0: 0, 1: 1}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib_dyn(n):
    return fib_rec(n)

# print(fib_dyn(10))

# Memoization can also be implemented
# as a class decorator

class Memoize:
 def __init__(self, fn):
  self.fn = fn
  self.memo = {}
 def __call__(self, arg):
  if arg not in self.memo:
   self.memo[arg] = self.fn(arg)
   return self.memo[arg]
 
@Memoize
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

# print fib(5)

def fib_iter(n):
    ret = [1, 1] + [0]*(n-2)
    for i in range(2,n,1):
        ret[i] = ret[i-1] + ret[i-2]
    return ret[-1]

# print(fib_iter(10))

def fib_iter_2(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

# print(fib_iter_2(10))

"""
RUN THE CODE BELOW TO TEST YOUR SOLUTION.
"""

class TestFib(object):
    def test(self,solution):
        assert solution(10) == 55
        assert solution(1) == 1
        assert solution(23) == 28657
        print 'Passed all tests.'
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()
methods = [fib_rec, fib_dyn, fib_iter, fib_iter_2, fib]
for f in methods:
    t.test(f)