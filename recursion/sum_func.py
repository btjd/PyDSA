def sum_func(n):
    """
    Given an integer, create a function 
    which returns the sum of all the 
    individual digits in that integer. 
    For example: if n = 4321, return 4+3+2+1
    """
    if n < 10:
        return n
    else:
        return n%10 + sum_func(n//10)

def test_sumfunc():
    assert sum_func(1234) == 10