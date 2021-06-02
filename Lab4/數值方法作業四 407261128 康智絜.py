import numpy as np
import math
import matplotlib.pyplot as plt

n = 45 	# 數據的數量

X = np.array([ 
		0.02000,0.08000,0.34000,0.45000,0.58000,0.70000,0.82000,1.07000,1.38000,1.68000,
		1.80000,1.93000,2.23000,2.50000,2.71000,2.86000,3.14000,3.40000,3.62000,3.88000,
		4.21000,4.45000,4.53000,4.71000,5.03000,5.18000,5.31000,5.43000,5.54000,5.80000,
		6.03000,6.16000,6.32000,6.45000,6.75000,6.95000,7.11000,7.25000,7.51000,7.73000,
		8.02000,8.16000,8.38000,8.61000,8.75000 ])
Y = np.array([ 
		1.00000,1.09530,1.47890,1.65150,1.84740,1.96420,2.09250,2.08640,1.69780,1.12560,
		0.89460,0.70720,0.54260,0.73960,1.04280,1.27990,1.66240,1.81770,1.78750,1.63360,
		1.44530,1.34830,1.33800,1.33330,1.30890,1.25790,1.19160,1.11650,1.04140,0.88350,
		0.84900,0.89830,1.04160,1.20370,1.68590,1.96220,2.09290,2.12590,1.94030,1.57880,
		1.00830,0.77950,0.56620,0.57930,0.67470 ])

#return Pm(x) coefficient y = a0 + a1*x + a2*x^2 ...
def get_coefficient(m):
	dim = m + 1	# 矩陣的維度
	A = np.zeros((dim, dim))
	B = np.zeros((dim, 1))

	A[0][0] = n
	# 求矩陣A
	for i in range (dim):
		for j in range (dim):
			for x in X:
				if i != 0 and j!= 0:
					A[i][j] += pow(x, (i+j))

	# 求矩陣B
	for i in range (dim):
		for j in range(n):
			B[i] += Y[j] * pow(X[j], i)

	# 回傳 Ax = B 中的 x
	return np.linalg.solve(A, B)

# Pm = m次多項式
def Pm(m, x):
	# 取得m次多項式的係數
	coeff = get_coefficient(m)
	ans = 0
	for i in range(m):
		ans += coeff[i]* math.pow(x, i)
	#回傳m次多項式帶入x後的結果
	return ans

# 計算誤差
def error(m):
	e = 0
	for i in range(n):
		e += (Pm(m, X[i]) - Y[i])**2

	return math.sqrt(e / (n-m))

def drawGraph(minPm):
	line_x = np.linspace(0.0, 10.0, 100)		# x從 0 ~ 10 間隔 0.1
	line_y = [ Pm(minPm, x) for x in line_x ]	# 將x代入Pm
	plt.title(f'The Best Choice is P{minPm}(x)', fontsize = 20)	# 標題
	plt.axis([0,10,0,5])						# 設定x, y座標的範圍( X:0~10 ; Y:0~5 )
	plt.xlabel('X', fontsize=16)			# X軸標題
	plt.ylabel('Y', fontsize=16, rotation=0)	# Y軸標題 並將標題方向轉正
	plt.scatter(X, Y, color='green')		# 印出原先的數據(綠色的圓點)
	plt.plot(line_x, line_y, color='red')		# 畫線
	plt.show()					# 顯示繪製的圖形

def main():

	num = 15 			# 找出 15次到(n-1)次的所有多項式
	minError = error(num)		# 最小的誤差
	minPm = num 			# 最小的誤差的minPm次多項式
	for m in range(num+1, n):	# 找15 ~ 44次多項式中最小誤差的多項式
		e = error(m)
		if e < minError:
			minError = e
			minPm = m

	print( "The Best Choice is P%d(x)" %minPm )		# 印出第幾次多項式是最好的
	print( "P%d(x)'s" %minPm, "error is", error(minPm) )	# 印出誤差最小的多項式的誤差
	drawGraph(minPm)			# 畫圖

if __name__ == '__main__':
	main()
