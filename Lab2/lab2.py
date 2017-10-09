from cvxopt.solvers import qp
from cvxopt.base import matrix # Converts normal mtx to cvxopt mtx

import numpy, pylab, random, math

tpe = "R"
c = 1

# Generate data to be used for computing a hyperplane
def gen_data():
	# Uncomment the line below to generate
	# the same dataset over and over again.
	numpy.random.seed(100)
	classA = [(random.normalvariate(-1.0,1),
		   	random.normalvariate(0.5,1),
		   	1.0)
			for i in range (5)] + \
			[(random.normalvariate(1.0,1),
			random.normalvariate(0.5,1),
			1.0)
			for i in range (5)]

	classB = [(random.normalvariate(0.0,1),
			random.normalvariate(0.5,1),
			-1.0)
			for i in range (10)]
	data = classA + classB
	random.shuffle(data)
	return data, classA, classB

# Kernel functions
def kernel(x, y, p=1, sigma=1, k = -10, delta = 0):
	if tpe == "L" or tpe == "P":
		return (numpy.dot(numpy.transpose(x),y)+1)**p
	elif tpe == "R":
		return math.exp(-(numpy.dot(numpy.subtract(x,y),numpy.subtract(x,y))/(2*sigma**2)))
	elif tpe == "S":
		return numpy.tanh(k*numpy.dot(numpy.transpose(x),y)-delta)

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

# Extract all alpha's that are larger than 0
def alphaX(data, alpha):
	lst = []
	epsilon = 10e-05
	for i in range(len(alpha)):
		if abs(alpha[i]) > epsilon:
			lst.append((data[i][0], data[i][1], data[i][2], alpha[i]))
	return lst

# Classifies a datapoint
def indicator(xs, ys, alpha_x):
	res = 0
	for (x, y, t, alpha) in alpha_x:
		res += alpha*t*kernel([xs, ys], [x, y])
	return res

def main():
	data, classA, classB = gen_data()


	# Vector q, vector h, matrix G
	q = [(-1.0) for i in range (20)]

	#h =[0.0 if i < 20 else c for i in range (40)]
	h =[0.0 for i in range (20)]

	G = numpy.identity(20)*(-1.0)


	Gs = []
	for x in range(40):
		tmp = []
		for y in range(20):
			print("x:", x, "y: ",y)
			if x == y:
				tmp.append(-1.0)
			elif x == y+20:
				tmp.append(1.0)
			else:
				tmp.append(0.0)
		Gs.append(tmp)

	#G = numpy.array(Gs)

	#print(G1)
	P = create_matrix_P(data)

	# Calculate alpha
	r = qp(matrix(P) , matrix(q) , matrix(G) , matrix(h))
	alpha = list(r['x'])

	alpha_x = alphaX(data, alpha)

	xrange=numpy.arange(-4,4,0.05)
	yrange=numpy.arange(-4,4,0.05)
	grid=matrix ([[indicator(x,y,alpha_x)
				for y in yrange ]
				for x in xrange ])

	print(grid)


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
	pylab.hold(False)
	pylab.show()

main()
