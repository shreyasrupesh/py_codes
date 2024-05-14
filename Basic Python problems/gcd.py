#gcd, geeksforgeeks
class Solution:
    def gcd(self, a : int, b : int) -> int:
      while b:
         a,b = b,a%b
      return a