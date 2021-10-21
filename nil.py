#Problem No. 36:
def compute():
	ans = sum(i for i in range(1000000) if is_decimal_binary_palindrome(i))
	return str(ans)


def is_decimal_binary_palindrome(n):
	s = str(n)
	if s != s[ : : -1]:
		return False
	t = bin(n)[2 : ]
	return t == t[ : : -1]


if __name__ == "__main__":
	print(compute())
  
  #Problem No. 37 :
  import eulerlib, itertools


def compute():
	ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
	return str(ans)


def is_truncatable_prime(n):
	# Test if left-truncatable
	i = 10
	while i <= n:
		if not eulerlib.is_prime(n % i):
			return False
		i *= 10
	
	# Test if right-truncatable
	while n > 0:
		if not eulerlib.is_prime(n):
			return False
		n //= 10
	return True


if __name__ == "__main__":
	print(compute())
