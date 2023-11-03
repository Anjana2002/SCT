
X ={}
Y ={}
Z ={}
comp = {}
Xcomp = {}
Ycomp = {}
inter = {}
flag = 0
print('Enter the fuzzy set X')
for i in range(1,5):
    X[i] = float(input("Enter the memership function of X"))

print('Enter the fuzzy set Y')
for i in range(1,5):
    Y[i] = float(input("Enter the memership function of Y"))


print('Union')
for i in X and Y:
    Z[i]=max(X[i],Y[i])  
print(Z)

print('Intersection')
for i in X and Y:
     if(X[i]<Y[i]):
        Z[i]=X[i]    
     else:
        Z[i]=Y[i]
print(Z)

print('Compliment of X')
for i in X:
    Z[i]=round(1-X[i],2)
print(Z)

print('Algebraic Sum ')
for i in X and Y:
    Z[i]=round(X[i]+Y[i]-X[i]*Y[i],2)
print(Z)

print('Bounded Sum')
for i in X and Y:
    Z[i]=min(1,X[i]+Y[i])
print(Z)

print('Bounded Difference')
def bd(X,Y):
    for i in X and Y:
        Z[i]=max(0,X[i]-Y[i])
bd(X,Y)
print(Z)

print('DeMorgans Law')
#XUY
for i in X and Y:
    Z[i]=max(X[i],Y[i])  
#(XUY)'
for i in Z:
    comp[i] = 1-Z[i]
#X' Y'
for i in X and Y:
    Xcomp[i] = 1-X[i]
    Ycomp[i] = 1-Y[i]
#X'intersection Y'
for i in Xcomp and Ycomp:
    inter[i] = min(Xcomp[i], Ycomp[i])
print(comp)
print(inter)
for i in comp and inter:
    if comp[i]==inter[i]:
        continue
    else:
        flag = 1
if(flag==0):
    print('DeMorgan Law satisified in case of union')
else:
    print('DeMorgan Law is not satisified in case of union')
#DeMorgan Law
#X intersection Y
for i in X and Y:
    Z[i]=min(X[i],Y[i])  
#(X intersection Y)'
for i in Z:
    comp[i] = 1-Z[i]
#X' Y'
for i in X and Y:
    Xcomp[i] = 1-X[i]
    Ycomp[i] = 1-Y[i]
#X'U Y'
for i in Xcomp and Ycomp:
    inter[i] = max(Xcomp[i], Ycomp[i])
print(comp)
print(inter)
for i in comp and inter:
    if comp[i]==inter[i]:
        continue
    else:
        flag = 1
if(flag==0):
    print('DeMorgan Law satisified in case of intersection')
else:
    print('DeMorgan Law is not satisified in case of intersection')

