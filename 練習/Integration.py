import numpy as np

def f(x):
	return 1 / (1 + x**2)

def Trapezoidal_Rule(a, b, n):
	delta_X = (b-a)/n 	# ΔX is the distance between Xi and X(i+1)

	X = []	# store X0 ~ Xn
	for i in range(n+1):
		X.append( a + delta_X*i )	# Xi = a + i * ΔX

	tmp = 0	# to store sum of f(X0) + 2*f(X1) + 2*f(X2) + ... + 2*f(Xn-1) + f(Xn)

	for i, j in zip(range(n+1), X):

		if i == 0 or i == n:
			tmp += f(j)			# f(X0) and f(Xn)
		else:
			tmp += 2 * f(j)		# 2*f(X1) + 2*f(X2) + ... + 2*f(Xn-1)

	return ( delta_X / 2 ) * tmp	# ΔX/2*( f(X0) + 2*f(X1) + 2*f(X2) + ... + 2*f(Xn-1) + f(Xn) )

# n is even
def Simpson_one_third_Rule(a, b, n):
	delta_X = (b-a)/n  	# ΔX is the distance between Xi and X(i+1)

	X = []	# store X0 ~ Xn
	for i in range(n+1):
		X.append( a + delta_X*i )	# Xi = a + i * ΔX

	tmp = 0	 # to store sum of f(X0) + 4*f(X1) + 2*f(X2) + 4*f(X3) + ... + 2*f(Xn-2) + 4*f(Xn-1) + f(Xn)

	for i, j in zip(range(n+1), X):

		if i == 0 or i == n:
			tmp += f(j)		# f(X0) and f(Xn)
		elif i % 2 == 0:
			tmp += 2 * f(j)	# 2*f(X2) + 2*f(X4) + ... + 2*f(Xn-2)
		elif i % 2 == 1:
			tmp += 4 * f(j)	# 4*f(X1) + 4*f(X3) + ... + 4*f(Xn-1)

	return ( delta_X / 3 ) * tmp	# ΔX/3*( f(X0) + 4*f(X1) + 2*f(X2) + 4*f(X3) + ... + 2*f(Xn-2) + 4*f(Xn-1) + f(Xn) )

# n must be multiple of 3
def Simpson_three_eighths_Rule(a, b, n):
	delta_X = (b-a)/n  # ΔX is the distance between Xi and X(i+1)

	X = []	# store X0 ~ Xn
	for i in range(n+1):
		X.append( a + delta_X*i )	# Xi = a + i * ΔX

	tmp = 0		# to store sum of (f(X0) + f(Xn))+ 2 * (f(X3) + f(X6) + ... ) + 3 * (f(X1) + f(X2) + f(X4) +...)

	for i, j in zip(range(n+1), X):

		if i == 0 or i == n:
			tmp += f(j)			# f(X0) + f(Xn)
		elif i % 3 == 0:
			tmp += 2 * f(j)		# 2 * (f(X3) + f(X6) + ... )
		else:
			tmp += 3 * f(j)		# 3 * (f(X1) + f(X2) + f(X4) +...)

	return ( 3 * delta_X / 8 ) * tmp	# (3*ΔX/8)*((f(X0) + f(Xn))+ 2*(f(X3) + f(X6) + ... ) + 3*(f(X1) + f(X2) + f(X4) +...))

def main():
	a = 0
	b = 6
	n = 6
	print("a =", a, ", b =", b, ", n =", n)
	print( "Trapezoidal_Rule:", Trapezoidal_Rule(a, b, n) )
	print( "Simpson_one_third_Rule:", Simpson_one_third_Rule(a, b, n) )
	print( "Simpson_three_eighths_Rule:", Simpson_three_eighths_Rule(a, b, n) )


if __name__ == '__main__':
	main()