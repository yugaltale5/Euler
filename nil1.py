#add
#Problem 52
import itertools


def compute():
	cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))
	ans = next(i for i in itertools.count(1) if cond(i))
	return str(ans)


if __name__ == "__main__":
	print(compute())

	
#problem 57
def compute():
	LIMIT = 1000
	ans = 0
	numer = 0
	denom = 1
	for _ in range(LIMIT):
		numer, denom = denom, denom * 2 + numer
		# Now numer/denom is the i'th (0-based) continued fraction approximation of sqrt(2) - 1
		if len(str(numer + denom)) > len(str(denom)):
			ans += 1
	return str(ans)


if __name__ == "__main__":
	print(compute())
