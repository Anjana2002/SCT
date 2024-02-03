# Write a Program to implement Union, Intersection and Complement operations in fuzzy set.
Z ={}
def union(A, B):
    for x in A and B:
        Z[x] = max(A[x], B[x])
    return Z
def intersection(A, B):
    for x in A and B:
        Z[x] = min(A[x], B[x])
    return Z
def compliment(X):
    for x in X:
        Z[x] = round(1-X[x],2)
    return Z
A = {}
B = {}

no_items = int(input('Enter the no of elements: '))
for _ in range(no_items):
    key = int(input('Enter the crispy set elements: '))
    A[key] = float(input('Enter the membership value of ' + str(key) + 'for first set: '))
    B[key] = float(input('Enter the menbership value of ' + str(key) + 'for second set: '))
print('A = ',A)
print('B = ',B)
print('Union ',union(A, B))
print('Inersection: ',intersection(A, B))
print('Compliment of A: ',compliment(A))
