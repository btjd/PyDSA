class memoize:
    def __init__(self, func):
        self.func = func
        self.known_keys = []
        self.known_values = []

    def __call__(self, *args, **kwargs):
        key = (args, kwargs)

        if key in self.known_keys:
            i = self.known_keys.index(key)
            return self.known_values[i]
        else:
            value = self.func(*args, **kwargs)
            self.known_keys.append(key)
            self.known_values.append(value)

            return value

# Top down / recursion + memoization method
@memoize
def coin_change(coin_list,price):
   min_coins = price
   if price in coin_list:
     return 1
   else:
      for coin in [c for c in coin_list if c <= price]:
         num_coins = 1 + coin_change(coin_list, price - coin)
         min_coins = min(num_coins, min_coins)
   return min_coins

# Bottom up / iterative + tabulation method
def coin_change_dp(coin_list, price):
    cache = [0] * (price + 1)
    # In the outer loop we iterate through all
    # the possible prices up to our price.
    for cents in range(price+1):
        # We need to keep the current figure
        # in a separate variable for further
        # comparison in line 50 (min_coins, after
        # comparison, could be (cents) or (cents-coin)+1)
        min_coins = cents
        # For every coing under our current price...
        for coin in [c for c in coin_list if c <= cents]:
            # Check to see which one is greater, making
            # change with coins equating cents (all 1s)
            # or 1 coin added to (cents) minus the current 
            # denomination (coin), it's min value should
            # already be cached through tabulation.
            min_coins = min(cache[cents - coin] + 1, min_coins)
        cache[cents] = min_coins
    return cache[price]

class TestCoinChange(object):
    
    def test_coin_change(self,solution):
        assert solution([1,5,10,25],63) == 6
        assert solution([1,5,10,21,25],63) == 3
        assert solution([1,5,10,25], 45) == 3
        assert solution([1,5,10,25], 23) == 5
        assert solution([1,5,10,25], 74) == 8
        
        print 'PASSED ALL TEST CASES!'
        
# Run Tests
t = TestCoinChange()
methods = [coin_change, coin_change_dp]
for f in methods:
    t.test_coin_change(f)