class PrimeNumber:
    @staticmethod
    def prime_number(n: int) -> int:
        """
        This function returns the nth prime number
        """
        primes = [2]
        num = 3
        while len(primes) < n:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num += 1
        return primes[-1]