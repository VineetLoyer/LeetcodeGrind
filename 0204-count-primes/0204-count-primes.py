class Solution:
    def countPrimes(self, n: int) -> int:
        # Create a boolean array isPrime of size N, initialized to True. (all numbers are assumed to be prime at first)
        # Start from 2, and for each prime, mark all its multiples as not prime (set them to False)
        #starting from p^2. Repeat this up to root(N)
        # at the end, the indices that remain True are prime numbers 

        if n<2:
            return 0
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j]=False
        return sum(is_prime)