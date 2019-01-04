def rec_sum(n):
    """
    Write a recursive function which
    takes an integer and computes the 
    cumulative sum of 0 to that integer.
    """
    if n == 1:
        return 1
    else:
        return n + rec_sum(n-1)

def test_recsum():
    assert rec_sum(4) == 10