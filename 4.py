def is_Palindrome(n):
	temp = n
	rev = 0
	while(n > 0):
		dig = n % 10
		rev = rev * 10 + dig
		n = n // 10
	if(temp==rev):
		return True
	else:
		return False


num1, num2, max_pal = 1, 1, 1
for i in xrange(101, 1000):
    for j in xrange(101, 1000):
	num = i * j
	if is_Palindrome(num):
	    if max_pal < num:
	        num1, num2, max_pal = i, j, num
#print num1, num2, max_pal
print num1, num2, max_pal
 #project euler


 #problem33
import math


def compute():
	numer = 1
	denom = 1
	for d in range(10, 100):
		for n in range(10, d):
			n0 = n % 10
			n1 = n // 10
			d0 = d % 10
			d1 = d // 10
			if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
				numer *= n
				denom *= d
	return str(denom // math.gcd(numer, denom))


if __name__ == "__main__":
	print(compute())

