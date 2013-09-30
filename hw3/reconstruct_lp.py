from cvxopt import matrix
from cvxopt.lapack import gesv
#constraints of the an LP. with decision variables x1...x8
constraints= [[1,0,0,1],[-2,-1,0,1],[1,3,-1,1],[0,-1,2,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#bVector = [[-2],[-1],[12],[15]]
bVector = [-2,-1,12,15] 
bMatrix = matrix(bVector,tc='d')

def matrixForBasics(basis):
    _matrix = []
    for index in basis:
        _matrix.append(constraints[index-1])    
    return matrix(_matrix,tc='d')

def solveLinearAlgebra(basis):
    A = matrixForBasics(basis)
    x = +bMatrix
    print "The Basis: ",basis 
    try:
        gesv(A,x)
        for i,xi in enumerate(x):
            print("X%-20s : %5.2f" %  (basis[i],xi))
        print "\n"
    except ArithmeticError:
        print "A is a singlar matrix. Cannot re-construct with the given basis\n"

solveLinearAlgebra([2,3,4,8])
solveLinearAlgebra([1,3,4,8])
solveLinearAlgebra([1,2,5,8])
solveLinearAlgebra([2,3,4,5])
solveLinearAlgebra([1,2,7,8])
