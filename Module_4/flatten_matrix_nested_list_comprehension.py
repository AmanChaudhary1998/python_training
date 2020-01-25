# Suppose I want to flatten a given 2-D list:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix = []
for sublist in matrix:
     for val in sublist:
          flatten_matrix.append(val)
print(flatten_matrix)
# Nested List Comprehensive to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
