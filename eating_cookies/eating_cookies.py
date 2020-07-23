'''
Input: an integer
Returns: an integer
'''
from time import time

def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if cache is None:
        cache = [0] * (n + 1)
    if cache[n] > 0:
        return cache[n]
    
    cache[n] = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)

    return cache[n]

# def eating_cookies_naive(n, cache={}):
#     print(n)
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0

#     return eating_cookies_naive(n - 3, cache) + eating_cookies_naive(n - 2, cache) + eating_cookies_naive(n - 1, cache)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    start = time()
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    end = time()
    print(f"Time run: {end - start}")
