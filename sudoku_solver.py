from simpleai.search import CspProblem, backtrack
import math
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper()
#possible dimensions: 4, 9, 16
dimension = 9

column_names = alphabet[:dimension]
row_names = list(range(1,dimension+1))



variables = tuple([str(column) + str(row) for column in row_names for row in column_names])
vars=[[variables[j * dimension + i] for j in range(dimension)] for i in range(dimension)]


values = row_names
#print(vars)
domains={}

for cel in variables:
    domains[cel] = values

#print(domains)
domains['1a'] = [2]
domains['1b'] = [7]
domains['1i'] = [5]
domains['2a'] = [1]
domains['2d'] = [2]
domains['2f'] = [5]
domains['3c'] = [6]
domains['3f'] = [3]
domains['3i'] = [1]
domains['4d'] = [4]
domains['4h'] = [2]
domains['5c'] = [5]
domains['5g'] = [9]
domains['5h'] = [6]
domains['5i'] = [8]
domains['6i'] = [3]
domains['7e'] = [4]
domains['7h'] = [9]
domains['8a'] = [4]
domains['8c'] = [2]
domains['8d'] = [8]
domains['9a'] = [6]
domains['9b'] = [3]
domains['9f'] = [9]
domains['9h'] = [7]


def constraint_unique(variables, values):
    # check if all the values are unique
    if len(values) == len(set(values)): # remove repeated values and count
        return True
    else:
        return False


def create_constraints(variables, dimension):
    constraints=[]
    constraints+=create_row_constraints(variables, dimension)
    constraints+=create_column_constraints(variables, dimension)
    constraints+=create_square_constraints(variables, dimension)

    return constraints

def create_row_constraints(variables, dimension):
    return [tuple(variables[i * dimension + j] for j in range(dimension)) for i in range(dimension)]
def create_column_constraints(variables, dimension):
    return [tuple(variables[j * dimension + i] for j in range(dimension)) for i in range(dimension)]
def create_square_constraints(variables, dimension):
    sub_squares = [
        tuple(vars[i][j] for i in range(row, row + int(dimension**0.5)) for j in range(col, col + int(dimension**0.5)))
        for row in range(0, dimension, int(dimension**0.5))
        for col in range(0, dimension, int(dimension**0.5))
    ]
    return sub_squares
    
cons = create_constraints(variables, dimension)
constraints=[]
for con in cons:
    constraints.append((con, constraint_unique))
    
problem = CspProblem(variables, domains, constraints)

output = backtrack(problem)
print('\nSolutions:', output)