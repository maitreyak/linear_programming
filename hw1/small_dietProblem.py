from cvxopt import solvers,matrix,spmatrix

food = ['Rice','Quinoa','Tortilla','Lentils','Broccoli']

nutrient = ['carbs','protein','fat'] 

nutrient_fact = matrix([[53,4.4,0.4],[40,8,3.6],[12,3,2],[53,12,0.9],[6,1.9,0.3]],tc='d')

#print nutrient_fact
cost = [0.5,0.9,0.1,0.6,0.4]

food_cost = matrix(cost, tc='d')

#print food_cost

max_nutrient = matrix([1000,100,100], tc='d')

min_nutrient = matrix([100,10,0],tc='d')

#print max_nutrient
#print min_nutrient


count_d_vars = 5

Id = spmatrix(1.0,range(count_d_vars),range(count_d_vars),(count_d_vars,count_d_vars))

constraint_lhs = matrix([nutrient_fact,-nutrient_fact,-Id])

constraint_rhs = matrix([max_nutrient,-min_nutrient,matrix(0.0,(count_d_vars,1))])

sol = solvers.lp(food_cost, constraint_lhs, constraint_rhs)

x = sol['x']

objective_value = 0.0 

for i,xi in enumerate(x):
     print("%-20s : %5.2f" %  (food[i],xi))
     if xi > 1e-6:
        objective_value += xi*cost[i]              

print "Objective value: %r" %(objective_value)
