from cvxopt import solvers,matrix,spmatrix

food = ['Rice','Quinoa','Tortilla','Lentils','Broccoli']

nutrient = ['carbs','protein','fat'] 

nutrient_fact = matrix([[53,4.4,0.4],[40,8,3.6],[12,3,2],[53,12,0.9],[6,1.9,0.3]],tc='d')

#print nutrient_fact
cost = [0.5,0.9,0.1,0.6,0.4]
protien_list = [4.4,8,3,12,1.9]
protein = matrix(protien_list,tc='d')

food_cost = matrix(cost, tc='d')

food_const = matrix([[0.9],[0.5],[0.1],[0.6],[0.4]],tc='d')

print food_cost
print nutrient_fact

max_nutrient = matrix([1000,100,100], tc='d')

min_nutrient = matrix([100,10,0],tc='d')

#print max_nutrient
#print min_nutrient

count_d_vars = 5

Id = spmatrix(1.0,range(count_d_vars),range(count_d_vars),(count_d_vars,count_d_vars))

constraint_lhs = matrix([nutrient_fact,-nutrient_fact,-Id,food_const])

constraint_rhs = matrix([max_nutrient,-min_nutrient,matrix(0.0,(count_d_vars,1)),matrix([2],tc='d')])

sol = solvers.lp(-protein, constraint_lhs, constraint_rhs)

x = sol['x']

objective_value = 0.0 

for i,xi in enumerate(x):
     print("%-20s : %5.2f" %  (food[i],xi))
     if xi > 1e-6:
        objective_value += xi*protien_list[i]              

print "Objective value: %r" %(objective_value)
