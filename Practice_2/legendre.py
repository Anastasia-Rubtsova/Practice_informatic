def max_power(n, k):
    def prime_factorization(x):
        factors = {}
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors[d] = factors.get(d, 0) + 1
                x //= d
            d += 1
        if x > 1:
            factors[x] = factors.get(x, 0) + 1
        return factors

    def legendre(n, p):
        count = 0
        power = p
        while power <= n:
            count += n // power
            power *= p
        return count

    k_factors = prime_factorization(k)
    min_power = float('inf')

    for prime, exp_in_k in k_factors.items():
        exp_in_n_fact = legendre(n, prime)
        possible_power = exp_in_n_fact // exp_in_k
        min_power = min(min_power, possible_power)

    return min_power

print(max_power(10, 2))  
print(max_power(10, 10))
print(max_power(25, 6))
