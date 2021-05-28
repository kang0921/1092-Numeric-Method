import math
import time

epsilon = math.pow(10, -6)
epoch = math.pow(10, 8)

# function 1
def f1(x):
	return -2*x*x - 6*x + 3

def g1(x):
	return -3/(-2*x-6)

def f1_differential(x):
	return -4*x - 6

# function 2
def f2(x):
	return x*x - 5*x - 8

def g2(x):
	return 8/(x-5)

def f2_differential(x):
	return 2*x - 5

# function 3
def f3(x):
	return 2*x*x + x - 6

def g3(x):
	return 6/(2*x+1)

def f3_differential(x):
	return 4*x + 1

# function 4 共同題
def f4(x):
	return 4.98*math.cos(x) + 3.2*x*math.sin(2*x) -3*x + 2.9

def g4(x):
	return (4.98*math.cos(x)+3.2*x*math.sin(2*x)+2.9)/3

def g4(x):
	return (-2.9 - 4.98*math.cos(x))/(3.2*math.sin(2*x)-3)

def f4_differential(x):
	return 3.2*(2*x*math.cos(2*x) + math.sin(2*x)) - 4.98 * math.sin(x) - 3

# 二分法
def Bisection(a, b, f):
	if f(a) * f(b) >= 0:
		print("Assume incorrect a and b.")
	else:
		cnt = 0
		while abs(a-b) > 2*epsilon and cnt < epoch:
			cnt += 1
			m = (a+b)/2
			if f(a) * f(m) > 0 :
				a = m
			else:
				b = m
		print("Bisection solution is", (a+b)/2, ", step is", cnt)

# 假位法
def False_Position(a, b, f):
	if f(a) * f(b) >= 0:
		print("Assume incorrect a and b.")
	else:
		cnt = 0
		m = ( a*f(b) - b*f(a) ) / ( f(b) - f(a) )
		old = m
		while abs(f(m) - f(old)) >= epsilon or cnt == 0:
			cnt += 1
			old = m
			if f(a) * f(m) > 0 :
				a = m
			else:
				b = m
			m = ( a*f(b) - b*f(a) ) / ( f(b) - f(a) )
		print("False Position solution is", m,", step is", cnt)

def Modify_False_Position(a, b, f):
	if f(a) * f(b) >= 0:
		print("Assume incorrect a and b.")
	else:
		Fa = f(a)
		Fb = f(b)
		m = ( a * Fb - b * Fa) / ( Fb - Fa )
		cnt = 0
		while abs(f(m)) > epsilon and cnt < epoch:
			cnt += 1
			Fm = f(m)
			if Fa * Fm >= 0:
				a = m
				Fa = Fm
				Fb = Fb/2
				m = (a*Fb - b*Fa)/(Fb-Fa)
			else:
				b = m
				Fb = Fm
				Fa = Fa/2
				m = (a*Fb - b*Fa)/(Fb-Fa)

		print("Modify false position solution is", m, ", step is", cnt)

# 牛頓法
def Newton_Method(x, f, df):
	init = x
	delta = -(f(x)/df(x))
	cnt = 0
	while abs(delta) >= epsilon and cnt < epoch:
		cnt += 1
		delta = -(f(x)/df(x))
		x = x + delta
	print("Newton method solution is", x, ", step is", cnt ,", initial input value is", init)

# 割線法
def Secant_Method(x1, x2, f):
	cnt = 0
	while abs(x2-x1) > epsilon and cnt < epoch:
		cnt += 1
		x3 = x1 - ( (f(x1)*(x2-x1))/(f(x2)-f(x1)) )
		x1 = x2
		x2 = x3
	print("Secant method solution is", x2,", step is", cnt)

# 固定點法
def Fixed_Point_Method(x0, f, g):
	init = x0
	x1 = g(x0)
	cnt = 0
	while abs(x1 - x0) > epsilon and cnt < epoch:
		x0 = x1
		x1 = g(x0)
		cnt += 1
	print("Fixed point method solution is", x1,", step is", cnt, ", initial input value is", init)


def main():

	f1_a = -1
	f1_b = 2
	print("Function1: -2*x*x - 6*x + 3")
	Bisection(f1_a, f1_b, f1)
	False_Position(f1_a, f1_b, f1)
	Modify_False_Position(f1_a, f1_b, f1)
	Newton_Method(f1_a, f1, f1_differential)
	Secant_Method(f1_a, f1_b, f1)
	Fixed_Point_Method(f1_a, f1, g1)

	print("---------------------------------------------------------------")

	f2_a = -2
	f2_b = 2
	print("\nFunction2: x*x - 5*x - 8")
	Bisection(f2_a, f2_b, f2)
	False_Position(f2_a, f2_b, f2)
	Modify_False_Position(f2_a, f2_b, f2)
	Newton_Method(f2_a, f2, f2_differential)
	Secant_Method(f2_a, f2_b, f2)
	Fixed_Point_Method(f2_a, f2, g2)

	print("---------------------------------------------------------------")

	f3_a = 1
	f3_b = 5
	print("\nFunction3: 2*x*x + x - 6")
	Bisection(f3_a, f3_b, f3)
	False_Position(f3_a, f3_b, f3)
	Modify_False_Position(f3_a, f3_b, f3)
	Newton_Method(f3_a, f3, f3_differential)
	Secant_Method(f3_a, f3_b, f3)
	Fixed_Point_Method(f3_a, f3, g3)

	print("---------------------------------------------------------------")

	f4_a = -5
	f4_b = -2.5
	print("\nFunction4: 4.98*math.cos(x) + 3.2*x*math.sin(2*x) -3*x + 2.9")
	print("a =", f4_a, ", b =", f4_b)
	Bisection(f4_a, f4_b, f4)
	False_Position(f4_a, f4_b, f4)
	Modify_False_Position(f4_a, f4_b, f4)
	Newton_Method(-3, f4, f4_differential)
	Secant_Method(f4_a, f4_b, f4)
	Fixed_Point_Method(-4, f4, g4)

	print("---------------------------------------------------------------")

	f4_a = -2.5
	f4_b = -2
	print("\nFunction4: 4.98*math.cos(x) + 3.2*x*math.sin(2*x) -3*x + 2.9")
	print("a =", f4_a, ", b =", f4_b)
	Bisection(f4_a, f4_b, f4)
	False_Position(f4_a, f4_b, f4)
	Modify_False_Position(f4_a, f4_b, f4)
	Newton_Method(-2, f4, f4_differential)
	Secant_Method(f4_a, f4_b, f4)
	Fixed_Point_Method(-3, f4, g4)

	print("---------------------------------------------------------------")
	f4_a = 1
	f4_b = 2
	print("\nFunction4: 4.98*math.cos(x) + 3.2*x*math.sin(2*x) -3*x + 2.9")
	print("a =", f4_a, ", b =", f4_b)
	Bisection(f4_a, f4_b, f4)
	False_Position(f4_a, f4_b, f4)
	Modify_False_Position(f4_a, f4_b, f4)
	Newton_Method(1, f4, f4_differential)
	Secant_Method(f4_a, f4_b, f4)
	Fixed_Point_Method(1, f4, g4)

	print("---------------------------------------------------------------")
	f4_a = 3
	f4_b = 4
	print("\nFunction4: 4.98*math.cos(x) + 3.2*x*math.sin(2*x) -3*x + 2.9")
	print("a =", f4_a, ", b =", f4_b)
	Bisection(f4_a, f4_b, f4)
	False_Position(f4_a, f4_b, f4)
	Modify_False_Position(f4_a, f4_b, f4)
	Newton_Method(3, f4, f4_differential)
	Secant_Method(f4_a, f4_b, f4)
	Fixed_Point_Method(5, f4, g4)

	# print("---------------------------------------------------------------")
	# Fixed_Point_Method(-5, f4, g4)
	# Fixed_Point_Method(-4, f4, g4)
	# Fixed_Point_Method(-3, f4, g4)
	# Fixed_Point_Method(-2, f4, g4)
	# Fixed_Point_Method(-1, f4, g4)
	# Fixed_Point_Method(0, f4, g4)
	# Fixed_Point_Method(1, f4, g4)
	# Fixed_Point_Method(2, f4, g4)
	# Fixed_Point_Method(3, f4, g4)
	# Fixed_Point_Method(4, f4, g4)
	# Fixed_Point_Method(5, f4, g4)

if __name__ == '__main__':
	main()
