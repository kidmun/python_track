class Solution:
    def countOrders(self, n: int) -> int:
        return (factorial(n * 2) // (2**n)) % (10 ** 9 + 7)