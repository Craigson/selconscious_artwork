import scipy
import math
from scipy.special import ellipj

r = 50
a = 0.5
x = []
y = []
z = []

#ellipj returns sn,cn,dn,ph

for t in range(1,101):
	jacobi = scipy.special.ellipj(t,(a*a))
	x.append(r * (jacobi[0])*math.cos(a*t))
	y.append(r * (jacobi[0])*math.sin(a*t))
	z.append(r * jacobi[1])


print(x[1],y[1],z[1])
