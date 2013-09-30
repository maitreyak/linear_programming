#Consider the following LP:
#Objective function : max (2 x1 + 0 x2 + -x3)
#S.T 
#    -1 x1   -1 x2           <= +5
#     1 x1   -2 x2   +1 x3   <= -10
#     1 x1           -1 x3   <= -20
#     1 x1   +1 x2   +1 x3   <= +3
#     x1,x2,x3>=0
#Setup the auxiliary problem with the auxiliary variable x0 and find out the value of x0 in the optimal solution to
#the auxiliary problem. You may use your favorite solver to do so and report the answer to two decimal places.

#Solution:
#We need the solve build the auxiliary problem and solve.

#Auxiliary LP:
#Objective fcuntion: max (-1 x0)
#    -1 x1   -1 x2          +1 x4   -1 x0 = +5
#     1 x1   -2 x2   +1 x3  +1 x5   -1 x0 = -10
#     1 x1           -1 x3  +1 x6   -1 x0 = -20
#     1 x1   +1 x2   +1 x3  +1 x7   -1 x0 = +3
#     x0,x1,x2,x3,x4,x5,x6,x7>=0

#Below code solve the auxiliary LP
from cvxopt import matrix, solvers,spmatrix

A = matrix([ [-1, 1, 1, 1], [-1, -2, 0, 1] , [0,1,-1,1],[-1,-1,-1,-1] ],tc='d')
b = matrix([ 5, -10, -20, 3 ],tc='d')
c = matrix([ 0,0,0,-1],tc='d')

#Build a identity matrix to represent x0,x1,..xn >=0 or -x0...-xn<=0
Id = spmatrix(1.0,range(4),range(4),(4,4))
constraintLhs = matrix([A,-Id])
constraintRhs = matrix([b,matrix(0.0,(4,1))])

sol=solvers.lp(-c,constraintLhs,constraintRhs)
#list of decision variables
dvars = ['x1','x2','x3','x0']
for i,xi in enumerate((sol['x'])):
    print("%-20s : %5.2f" %  (dvars[i],xi))
