# Write a program to implement De-Morgan’s Law in Fuzzy sets.
Z = {}
def union(A, B):
    for x in A and B:
        Z[x] = max(A[x], B[x])
    return Z
def compliment(X):
    for x in X:
        Z[x] = round(1-X[x], 2)
    return Z
def intersection(A, B):
    for x in A and B:
        Z[x] = min(A[x], B[x])
    return Z
def get_membership(key):
    while True:
        value = float(input('Enter  the membership value (between 0 and 1) for  '+key))
        if 0<=value<=1:
            return value
        else:
            print("Invalid input. Please enter a value between 0 and 1.")
A = {}
B = {}

no = int(input('Enter the numbers :'))
for _ in range(no):
    key = input('enter the crispy set element:')
    value = get_membership(key)
    A[key] = value
    value = get_membership(key)
    B[key] = value

LHS = compliment(union(A, B))
RHS = intersection(compliment(A), compliment(B))
print(f'Fuzzy sets are {A=} an {B=}')
if LHS==RHS:
    print(f'DeMorgan is proved since {LHS}={RHS}' )

