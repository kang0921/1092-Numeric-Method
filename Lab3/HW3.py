import math

# 回傳積分中的f(x)
def f(x):
	return (1/math.sqrt(2*math.pi))*math.exp(-x*x/2)

# Simpson's 1/3 rule
# 參數x是normal dist.中積分的z
# 參數n是要切成幾份
def simpson(x, n):
	sum = 0
	delta = x/n 	# (b-a)/n
	for x in range(0, n+1):	 # x = 0~n 分別算出切成n份的面積

		# 如果是x0或xn 則f(x0)和f(xn)乘1倍
		if x == 0 or x == (n):	
			sum += f(x*delta)

		# 如果是xi的i是奇數 則f(xi)乘4倍
		elif x%2 == 1:
			sum += 4 * f(x*delta)

		# 如果是xi的i是偶數 則f(xi)乘2倍
		else:
			sum += 2 * f(x*delta)

	return (delta/3)*sum

def main():
	n = 100		#要切的間隔數
	offset = 0.001		# 方便計算.001~.009 如果要算.00n時 改這個變數即可
	for i in range(0, 500):
		print(round(simpson(0.01*i+offset, n)+0.5, 4) )		# 四捨五入到小數點第四位

if __name__ == '__main__':
	main()