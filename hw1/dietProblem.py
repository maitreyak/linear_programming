#The miniature version of the diet problem has n=5 foods and m=3 nutrients. 
#The foods considered are rice, quinoa, tortilla, lentils and broccoli . 
#The nutrients are carbohydrates, proteins and fat
#
#The caloric and pricing information (fictional) is as below:
#
#Food Name	 Carbs/Unit	 Proteins/Unit	 Fat/Unit	 Price/Unit
#Rice	        53	        4.4	            0.4	        0.5
#Quinoa	        40	        8	            3.6	        0.9
#Tortilla	    12	        3	            2	        0.1
#Lentils	    53	        12	            0.9	        0.6
#Broccoli	    6	        1.9	            0.3	        0.4

#The data on daily minimal and maximal requirements are below:
#
#Nutrient	        Minimum	 Maximum
#Carbohydrates	    100	        1000
#Protein	        10	        100
#Fat	            0	        100

#The following are the decision variables used:
#
#Food Name	 Decision Variable
#Rice	        xr
#Quinoa	        xq
#Lentils	    xl
#Tortilla	    xt
#Brocolli	    xb


from cvxopt import solvers,matrix,spmatrix

#Types of food
food = ['Rice','Quinoa','Tortilla','Lentils','Broccoli']
#count
foodCount = len(food)
#Types of nutrients 
nutrient = ['carbs','protein','fat'] 
#Facts about the food 
nutrientFact = [[53,4.4,0.4],[40,8,3.6],[12,3,2],[53,12,0.9],[6,1.9,0.3]]
#cost list
cost = [0.5,0.9,0.1,0.6,0.4]
#Matrix from of the above
costMatrix = matrix(cost,tc='d')
#Matrix from of the above
nutrientFactMatrix = matrix(nutrientFact,tc='d')

#max matrix
maxNut = [1000,100,100]
maxMatrix = matrix(maxNut,tc='d')

#min matrix
minNut = [100,10,0]
minMatrix = matrix(minNut,tc='d')


#prints the objective value
def objectiveValue(message,valueList,solution):
    obj_value = 0.0
    for i,xi in enumerate(solution):
         print("%-20s : %5.2f" %  (food[i],xi))
         if xi > 1e-6:
            obj_value += xi*valueList[i]              

    print "Objective value for %s is: %r" %(message,obj_value)


#plain jane diet problem
def simpleDietProblem():
    Id = spmatrix(1.0,range(foodCount),range(foodCount),(foodCount,foodCount))
    constraintLhs = matrix([nutrientFactMatrix,-nutrientFactMatrix,-Id])
    constraintRhs = matrix([maxMatrix,-minMatrix,matrix(0.0,(foodCount,1))])
    sol = solvers.lp(costMatrix, constraintLhs, constraintRhs)
    objectiveValue("Simple Diet Problem",cost,sol['x'])

def sixtyPercentDietProblem():
    #Build the 60% constreint matrix
    sixtyPercentCost= []
    for index1 in range(0,len(cost)):
        sixtyPercentCost.append([])
        for index2 in range(0,len(cost)):
            value = cost[index1] * -0.6
            if index1 == index2:
                value += cost[index1]
            sixtyPercentCost[index1].append(value)

    sixtyPercentCostMatrix = matrix(sixtyPercentCost,tc='d')

    Id = spmatrix(1.0,range(foodCount),range(foodCount),(foodCount,foodCount))
    constraintLhs = matrix([nutrientFactMatrix,-nutrientFactMatrix,-Id,sixtyPercentCostMatrix])
    constraintRhs = matrix([maxMatrix,-minMatrix,matrix(0.0,(foodCount,1)),matrix(0.0,(foodCount,1))])
    sol = solvers.lp(costMatrix, constraintLhs, constraintRhs)
    objectiveValue("Sixty Percent Diet Problem",cost,sol['x'])



if __name__ == "__main__":
    simpleDietProblem()
    sixtyPercentDietProblem()


