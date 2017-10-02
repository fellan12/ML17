from cvxopt.solvers import qp
from cvxopt.base import matrix # Converts normal mtx to cvxopt mtx

import numpy, pylab, random, math

tpe = "L"

def gen_data():
	# Uncomment the line below to generate
	# the same dataset over and over again.
	numpy.random.seed(100)
	classA = [(random.normalvariate(-10.5,1),
		   	random.normalvariate(0.5,1),
		   	1.0) 
			for i in range (5)] + \
			[(random.normalvariate(1.5,1),
			random.normalvariate(0.5,1), 
			1.0)
			for i in range (5)]

	classB = [(random.normalvariate(0.0,0.5),
			random.normalvariate(-10.5,0.5),
			-1.0)
			for i in range (10)]
	data = classA + classB
	random.shuffle(data)
	return data, classA, classB

# Kernel functions
def kernel(x, y, p=1, sigma=1):
	if tpe == "L" or tpe == "P":
		return (numpy.dot(numpy.transpose(x),y)+1)**p
	elif tpe == "R":
		return e**(((numpy.subtract(x,y))**2)/(2*sigma**2))

# Matrix P
def create_matrix_P(data):
	P = []
	for (x1_i, x2_i, t_i) in data:
		row = []
		for(x1_j, x2_j, t_j) in data:
			xi = numpy.array([x1_i, x2_i])
			xj = numpy.array([x1_j, x2_j])
			row.append(t_i*t_j*kernel(xi, xj))
		P.append(row)
	return P

def alpha_x(data, alpha):
	lst = []
	epsilon = 10e-05
	for i in range(len(alpha)):
		if abs(alpha) > epsilon:
			lst.append((data[i][0], data[i][1], data[i][2], alpha[i]))

def indicator(xs, ys):
	res = 0
	for (x, y, t, alpha) in lst:
		res += alpha*t*kernel([xs, ys], [x, y])
	return res

def main():
	data, classA, classB = gen_data()
	

	# Vector q, vector h, matrix G
	q = [(-1.0) for i in range (20)]
	h =[0.0 for i in range (20)]
	G = numpy.identity(20)*(-1)
	P = create_matrix_P(tpe, data)

	# Calculate alpha
	r = qp(matrix(P) , matrix(q) , matrix(G) , matrix(h))
	alpha = list(r['x'])

	alpha_x = alpha_x(data, alpha)

	xrange=numpy.arange(-4,4,0.05)
	yrange=numpy.arange(-4,4,0.05)
	grid=matrix ([[indicator(x,y)
				for y in yrange ]
				for x in xrange ])

	
	pylab.contour(xrange, yrange, grid,
					(-1.0, 0.0, 1.0),
					colors=('red', 'black', 'blue'),
					linewidths=(1, 3, 1))

	pylab.hold(True)
	pylab.plot([p[0] for p in classA],
				[p[1] for p in classA],
				'bo')
	pylab.plot([p[0] for p in classB],
	[p[1] for p in classB],
	'ro')
	pylab.show()














