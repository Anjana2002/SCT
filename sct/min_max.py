#find the min-max composition of 2 fuzzy sets

def min_max(X,Y):
    comp=[]
    for i in range(r1):
        comp.append([])
        for j in range(c2):
            result=[]
            for k in range(r2):
                result.append(min(X[i][k],Y[k][j]))
            comp[i].append(max(result))
    print("\n")
    print("Min-Max Combination")
    for i in range(r1):
        for j in range(c2):
            print(comp[i][j],end=" ")
        print("\n")

X =[]
Y =[]
print('fuzzy relation X')
r1= int(input('Enter the row: '))
c1= int(input('Enter the column: '))
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(float(input("Enter: ")))
    X.append(a)   
for i in range(r1):
    for j in range(c1):
        print(X[i][j], end = " ")
    print()

print('fuzzy relation Y')
r2= int(input('Enter the row: '))
c2= int(input('Enter the column: '))

for i in range(r2):
    a=[]
    for j in range(c2):
        a.append(float(input("Enter: ")))
    Y.append(a)   
for i in range(r2):
    for j in range(c2):
        print(Y[i][j], end = " ")
    print()

min_max(X,Y)




