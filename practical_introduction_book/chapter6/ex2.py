""" 

eratosphen algo 

"""
n = 100
primes = [True] * n
primes[0] = primes[1] = False

for i in range(2, n):
	if primes[i]:
		for j in range(2*i, n, i):
			primes[j] = False

for i in range(n):
	print(i, " is prime" if primes[i] else " isn't prime")
