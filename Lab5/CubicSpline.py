import numpy as np
import math

# data
X = np.array([0.2, 0.48, 1.32, 2.69, 3.57])
Y = np.array([3.7, 4.52, 5.28, 4.73, 5.86])
n = len(X)	# number of X

def init():
	
	# h[i] is the length of the i-th interval
	h = np.zeros(n)	# set initial values of h
	for i in range(n-1):
		h[i+1] = X[i+1] - X[i]	# h1, h2,..., h(n-1)

	A = [[0]*(n-2) for i in range(n-2)]		# initial A as 0
	
	# set the value of the first row of A
	A[0][0] = 2*(h[1]+h[2])	
	A[0][1] = h[2]

	# set the value of the row 2 to row n-3 of A
	for i in range(1, n-3):
		A[i][i-1] = h[i+1]
		A[i][i] = 2 * ( h[i+1] + h[i+2] )
		A[i][i+1] = h[i+2]

	# set the value of the last row of A
	A[n-3][n-4] = h[n-2]
	A[n-3][n-3] = 2 * ( h[n-2] + h[n-1] )

	B = [[0] for i in range(n-2)]	# initial B as 0

	# set the value of B
	for i in range(n-2):		
		B[i] = 6 * ( ((Y[i+2] - Y[i+1])/h[i+2]) - ((Y[i+1] - Y[i])/h[i+1]) )

	# S is the solution of Ax = B
	S = np.linalg.solve(A, B)
	return h, S

def CubicSpline(i, h, S):
	
	s = np.zeros(n+1)	# initial s0, s1, s2,..., sn as 0
	for j in range(2, n):
		s[j] = S[j-2]	# set s2 to sn-1

	# P3^i(X) = ai(X-Xi)^3 + bi(X-Xi)^2 + ci(X-Xi) + di
	a = (s[i+1] - s[i])/(6*h[i])
	b = s[i]/2
	c = (Y[i]-Y[i-1])/h[i] - ((2*s[i]+s[i+1])*h[i])/6
	d = Y[i-1]

	print("P3^%d(X) = %f(X-%.2f)^3 + %f(X-%.2f)^2 + %f(X-%.2f) + %f" %(i, a, X[i-1], b, X[i-1], c, X[i-1], d))


def main():
	h, S = init()
	for i in range(1, n):
		CubicSpline(i, h, S)

if __name__ == '__main__':
	main()